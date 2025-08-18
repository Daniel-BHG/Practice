fn main() {
    // hello will be stored at read-only binary memory,
    // so hard to anticipate the size at compile time
    let s_immutable = "hello"; 

    // it'll be stored at heap
    // call the memory allocator with String::from
    let mut s_mutable = String::from("hello");
    s_mutable.push_str(" world!");
    println!("{s_mutable}");

    let s1 = String::from("hello");
    println!("s1 : {s1}\n");
    // copy the pointer, length.. so both pointer point the same memory
    // so Rust considers the s1 is no longer valid
    let s2 = s1;
    // println!("s1 : {s1}"); // will get compile error

    let mut s3 = String::from("first mem");
    s3 = String::from("second mem"); // first mem will be freed right away
    println!("s3: {s3}\n"); // will print "second mem"

    // Deep copy = clone
    let s1 = String::from("deep copy");
    let s2 = s1.clone();
    println!("s1: {s1}, s2: {s2}"\n);

    // if integer, no need clone method as it's known size and can quickly copy
    let x = 5;
    let y = x;
    println!("x = {x}, y = {y}\n");

    let ownership2function = String::from("ownership2function");
    // after calling the function, the string is no longer valid because it's out of scope
    takes_ownership(ownership2function);
    let integer2function = 5;
    makes_copy(integer2function);

    // give ownership
    let give_ownership_s1 = gives_ownership(); // s1 will be dropped at out of scope
    println!("give_ownership_s1 = {give_ownership_s1}");
    let give_ownership_s2 = String::from("hello give_ownership_s2");
    // s2 loses the ownership when it moves to function
    let give_ownership_s3 = takes_and_gives_back(give_ownership_s2);  // s3 will be dropped at OOC
    println!("give_ownership_s3 = {give_ownership_s1}");

    // multiple function output
    let multi_s1 = String::from("multiple output function");
    // need multi_s2 because multi_s1 loses ownership
    let (multi_s2, len) = calculate_length(multi_s1); 
    println!("multiple output function : {multi_s2} {len}");

    // Reference borrowing
    let ref_s1 = String::from("reference");
    // ref_s1 will not be taken the ownership
    // however, it cannot change the value
    let ref_len = ref_calculate_length(&ref_s1);
    println!("reference: {ref_s1} {ref_len}");

    // mutable references : &mut string
    // however, cannot mutable for two variables in same referencing
    // let r1 = &mut s; let r2 = &mut s; -> Got compile error
    let mut mut_ref_s = String::from("mutable ref");
    mut_ref_change(&mut mut_ref_s);

    // dangling ref
    let referece2nothing = dangle_ref();
} // if the variable goes to out of scope, it is no longer valid by calling drop

// --------------------

fn takes_ownership(some_string: String) {
    println!("takes_ownership: {some_string}");
} // you can't use ownership2function again in the main function

fn makes_copy(some_integer: i32){
    println!("makes_copy the integer: {some_integer}");
} // nothing happens to integer2function variable

fn gives_ownership() -> String {
    let some_string = String::from("yours");
    some_string // return this String
}

fn takes_and_gives_back(a_string: String) -> String {
    a_string
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len();
    (s, length)
}

fn ref_calculate_length(s: &String) -> usize {
    s.len()
} // s goes out of scope but actually s doesn't have ownership

fn mut_ref_change(some_string: &mut String) {
    some_string.push_str(". it's mutable")
}

fn dangle_ref() -> String {
    let s = String::from("dangling reference");
    s
} // s goes out of scope so cannot borrow the s. 
// So return type should be &String -> String