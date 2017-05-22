#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <unistd.h>
#include <signal.h>
#include <sys/socket.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <linux/if.h>
#include <linux/if_ether.h>
#include <netinet/ip.h>
#include <netinet/in.h>
#include <netinet/tcp.h>
#include <netinet/ether.h>
#include <net/ethernet.h>
#include <net/if_arp.h>
#include <arpa/inet.h>

#define IF_NAME   "eth0"
#define PACKETSIZE 18 + 1500 /* Eth frame items + data up to 1500 octets */

/*
 * TODO
 *
 * in certain places (process_ip)  ntohs/ntohl might be user incorrect ...
 */


int sock_fd=0;
struct ifreq if_req_old;


int set_NIC(void);
static char *get_name(char *ip_addr);
static char *eth_frame_type(u_int16_t type);
static char *get_protocol(int proto);
void set_old_NIC(void);


void process_ip(unsigned char *buff, unsigned int len)
{  struct ip *ip_hdr;
   struct tcphdr *tcp; 
   unsigned int i=0;
     
     ip_hdr = (struct ip *) (buff + ETH_HLEN);
     printf("v%d hdr_len:%d tos:%u tot_len:%u id:%u frag.offs:%u ttl:%d ",
            ip_hdr->ip_v, ip_hdr->ip_hl*4, ntohs(ip_hdr->ip_tos), 
            ntohs(ip_hdr->ip_len), ntohs(ip_hdr->ip_id), 
            ntohs(ip_hdr->ip_off), ip_hdr->ip_ttl);
     printf("proto:%u (%s)\n",  ip_hdr->ip_p, 
             get_protocol(ip_hdr->ip_p));
     printf("SA:%s > ", inet_ntoa(ip_hdr->ip_src));
     printf("DA:%s\n", inet_ntoa(ip_hdr->ip_dst));

     if(ip_hdr->ip_p == IPPROTO_TCP) {
         // length of ip hdr padded .... 4
         tcp = (struct tcphdr *) (buff + ETH_HLEN + ip_hdr->ip_hl*4);
         printf("sp:%u dp:%u seq:%u ack_seq:%u header_len:%u\n",
         ntohs(tcp->source), ntohs(tcp->dest),
         ntohs(tcp->seq), ntohs(tcp->ack_seq),
         tcp->doff*4);
         printf("tcp data:....\n");
//       for(i=tcp->doff*4; i<len; i++) printf("%02X[%d]-", buff[i], buff[i]);
     }
     
} // process_ip()  


void catch_packet(int sock_fd) 
{
   unsigned int len=0, i=0;
   unsigned char buff[PACKETSIZE];
   struct ether_header *eth_hdr;
   struct ether_addr *eth_addr_d, *eth_addr_s;
   u_int16_t ether_type;
   
   while(1) {
      len = recvfrom(sock_fd, buff, PACKETSIZE, 0, NULL, NULL);    
      eth_hdr    = (struct ether_header *) buff;
      eth_addr_d = (struct ether_addr *) eth_hdr->ether_dhost;
      eth_addr_s = (struct ether_addr *) eth_hdr->ether_shost;
      ether_type = ntohs(eth_hdr->ether_type);
      
      printf("length: %d (%04X)\n", len, len);
      printf("Eth:  DA: %s   ", ether_ntoa(eth_addr_d));
      printf("SA: %s  ", ether_ntoa(eth_addr_s));
      printf("type: %04X (%s)\n", ether_type, eth_frame_type(ether_type)); 
      
      if(ether_type == ETHERTYPE_IP) {  // IP packet
        process_ip(buff, len);
      }   
      printf("\n\n");
      
    //  print all the received data ...
 //          for(i=0; i<len; i++)  printf("%02X[%d]-", buff[i], buff[i]);
   }
   
}  // catch_packet() 


/*
 * 
 * (signal function)  close_analyzer(int sig) -> sets NIC into previous state
 */
void close_analyzer(int sig)
{
  set_old_NIC();
  printf("Gracefull shutdown ... \n\n");
  exit(0);
}  
  

 
int main(void) 
{   
   if(signal(SIGINT, close_analyzer) == SIG_ERR) {  /* Ctrl-C signal  */
      printf("Cannot catch signal SIGINT, signal failed.");
   }
   
   sock_fd=set_NIC();
   catch_packet(sock_fd);
   return(0);
}


/*
 * get_name - get machine name according IP address, returns string
 */
static char *get_name(char *ip_addr) 
{ struct hostent *p_hent;
  char token[4];
 
  token[0] = atoi(strtok(ip_addr, "."));
  token[1] = atoi(strtok(NULL, "."));
  token[2] = atoi(strtok(NULL, "."));
  token[3] = atoi(strtok(NULL, "."));

  if((p_hent = gethostbyaddr(token, 4, AF_INET)) != NULL) {
     return (p_hent->h_name);
  } else return ("");
}   


/*
 * set_NIC - set NIC into promiscous mod, catching all packet on eth level
 */
int set_NIC()
{
   struct ifreq if_req;

   /* catch packets:  ETH_P_IP, ETH_P_ARP, ... */
   /* pouze IP, ARP packety, chytne je ale v ETH ramci (ETH header, atd) */
   if((sock_fd = socket(PF_PACKET, SOCK_RAW, htons(ETH_P_ALL))) == -1)  {
      perror("set_NIC: socket: failed open socket");
      exit(1);
   }
   strcpy(if_req.ifr_name, IF_NAME);
   
   if(ioctl(sock_fd, SIOCGIFFLAGS, (char *) &if_req) == -1) {
      perror("catch: set_NIC: ioctl: failed read NIC flags");
      exit(1);
   }   
   
   memcpy(&if_req_old, &if_req, sizeof(struct ifreq)); // backup origin state
   if_req.ifr_flags |= IFF_PROMISC; 
   
   if(ioctl(sock_fd, SIOCSIFFLAGS, (char *) &if_req) == -1) {
      perror("catch: set_NIC: ioctl: failed set NIC flags");
      exit(1);
   }
   return(sock_fd);
}  



void set_old_NIC()
{ struct ifreq if_req;

     strcpy(if_req.ifr_name, IF_NAME);
     memcpy(&if_req, &if_req_old, sizeof(struct ifreq));
     if (ioctl(sock_fd, SIOCSIFFLAGS, (char *) &if_req) < 0) {
         perror("set_old_NIC: ioctl: set old NIC flags failed");
         exit(1);
     }
}
 

/*
 * get_protocol - return name of a protocol according to input number
 */
static char *get_protocol(int proto)
{ struct protoent *pent;
    
    if((pent = getprotobynumber(proto)) != NULL) {
      return pent->p_name;
    }
    else 
      return "unknown";
  
} // get_protocol()  



/*
 * eth_frame_type - returns name of type of packet encapsulated in eth frame
 */ 
static char *eth_frame_type(u_int16_t type)
{  static char unknown[50];
   switch (type) {
     case  ETHERTYPE_PUP     :  return "Xerox PUP";    break;  // 0x0200
     case  ETHERTYPE_IP      :  return "IP";           break;  // 0x0800
     case  ETHERTYPE_ARP     :  return "ARP";          break;  // 0x0806
     case  ETHERTYPE_REVARP  :  return "Reverse ARP";  break;  // 0x8035
   }                              
   sprintf(unknown, "unknown frame type (%04X)", type);
   return(unknown);
}   


