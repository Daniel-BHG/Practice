fn main() {
    // enum - one of the multiple status
    let enum_only_name_v4 = IpAddrKind_only_name::V4;
    let enum_only_name_v6 = IpAddrKind_only_name::V6;

    // enum that has data type - more concise way
    let home_w_type = IpAddrKind_w_type::V4(String::from("127.0.0.1"));
    let loopback_w_type = IpAddrKind_w_type::V6(String::from("::1"));
    // more example
    let home_w_type_ex2 = IpAddrKind_w_type_ex2::V4(127, 0, 0, 1);
    let loopback_w_type = IpAddrKind_w_type::V6(String::from("::1"));

    // anotehr ex
    impl Message_ex1 {
        fn call (&self){
            // method body
        }
    }
    let m = Message_ex1::Write(String::from("hello"));
    m.call();

    // null of Rust, option
    // option은 값이 없을수도 있는 예외적인 상황을 처리하기 위해 필요
    // we need option type for handling the exceptional situation that the value may or may not exist
    // normally, it's used with 'match' and handle the None cases 
    enum Option<T> {
        None,
        Some(T), // T can be any type
    }
    let some_number = Some(5); // Option<i32>
    let some_char = Some("c"); // Option<char>
    let absent_number: Option<i32> = None; // don't have a valid value, but have a type
}

enum IpAddrKind_only_name {
    V4,
    V6,
}

// with struct, we need to define the address separately
// but with enum, we can do more concisely
struct IpAddr_for_compare {
    kind: IpAddrKind_only_name,
    address: String,
}
// like this
enum IpAddrKind_w_type {
    V4(String),
    V6(String),
}
// more examples
enum IpAddrKind_w_type_ex2 {
    V4(u8, u8, u8, u8),
    V6(String),
}

// another ex
enum Message_ex1 {
    Quit,
    Move { x: i32, y: i32},
    Write(String),
    ChangeColor(i32, i32, i32),
}