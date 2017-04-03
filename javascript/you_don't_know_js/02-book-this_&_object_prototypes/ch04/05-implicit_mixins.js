// implicit mixins

var Something = {
    cool: function() {
        this.greeting = "Hello World";
        this.count = this.count ? this.count + 1 : 1;
    }
};

Something.cool();
console.log(Something.greeting); // "Hello World"
console.log(Something.count); // 1

var Another = {
    count: 2,
    cool: function() {
        // implicit mixin of `Something` to `Another`
        // beheviour just like in chapter 1 - first explanation of this
        // and setting context of Another
        // advice to be avoided - results in code harder to maintain
        Something.cool.call(this);
    }
};

Another.cool();
console.log(Another.greeting); // "Hello World"
console.log(Another.count);  // not shared state with `Something`, prints 3

// in both explict (doing mixin) as well as here, the polymorphism is acheived
// via TargetObj.method.call(new_context_obj)
// here, no mixin at all


