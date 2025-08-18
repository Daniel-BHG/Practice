fn main() {
    // find the first blank
    let mut s = String::from("hello world");
    let word = first_word(&s); // borrow
    // s.clear(); // empties the string, meaning ""

    // string slices
    let string_slice = String::from("hello world");
    let string_len = string_slice.len();
    let hello = &string_slice[..5];
    let world = &string_slice[6..string_len];
    let whold_words = &string_slice[..]; // same as [0..string_len]

    // &str, &String
    let mystring = String::from("hello world");
    // slices of String
    let word = first_word(&mystring[0..6]);
    let word = first_word(&mystring[..]);
    let word = first_word(&mystring);

    let mystring_literal = "hello world";
    // slices of string literals
    let word = first_word(&mystring_literal[0..6]);
    let word = first_word(&mystring_literal[..]);
    // str are string slices already
    let word = first_word(mystring_literal);
}

// borrow the String
// return with string slice type : &str
fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();
    for (idx, &item) in bytes.iter().enumerate() {
        if item == b' '{
            return &s[..idx];
        }
    }
    &s[..] // need to use borrow type as the function borrows the variable
}

fn second_word(s: &String) -> (usize, usize) {

}