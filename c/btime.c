/* writes actual time into file specified in parameter, if file exists line 
 * is appended, if doesn't is created
 * Usage:  btime <full-path-to-out-file> 
 * linked static
 */

#include <stdio.h>
#include <time.h>


FILE *file_open(const char *filename, const char *mod) {
   FILE *fw;  
   if (( fw=fopen(filename, mod)) == NULL ) {
      fprintf(stderr, "Cannot open file %s!\n", filename);
      exit(1);
   }   
   return(fw);
}   

void file_close(FILE *file, const char *filename) {
int res;
   if (( res=fclose(file)) != 0 ) {
      fprintf(stderr, "Cannot close file %s!\n", filename);
      exit(1);
   }   
}   


int main(int argc, char *argv[]) {
     FILE *fw;
     time_t num_sec;
     char *my_time;

   if ( argc !=2 ) {
      fprintf(stderr, "No param! Usage:"
            "  %s <full-path-to-out-file>\n",argv[0]);
      return(1);
   }

   fw=file_open(argv[1], "a+");
   time(&num_sec);  /* returns amount of secs from 1st.Jan 1970 */
   my_time=ctime(&num_sec); /* secs into human readable "time string" */
   fprintf(fw,"Comp ups at:  %s", my_time);
   file_close(fw, argv[1]);
   
   return(0);
}   
   
