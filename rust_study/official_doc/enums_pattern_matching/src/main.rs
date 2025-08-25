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

    // Match control flow
    enum Coin_ex1{
        Penny,
        Nickle,
        Dime,
        Quarter,
    }
    fn value_in_cents_ex1(coin: Coin_ex1) -> u8 {
        match coin { // which one matches with the variable?
            Coin_ex1::Penny => { // return the multiple outputs
                println!("Lucky penny!");
                1
            } 
            Coin_ex1::Nickle => 5, // returns this value
            Coin_ex1::Dime => 10,
            Coin_ex1::Quarter => 25,
        }
    }

    // patterns that bind to values
    #[drive(Debug)] // for easily checking the status
    enum UsState_ex2 {
        Alabama,
        Alaska,
        SanFrancisco,
    }
    enum Coin_ex2 {
        Penny,
        Nickle,
        Dime,
        Quarter(UsState_ex2),
    }
    fn value_in_cents_ex2(coin: Coin_ex2) {
        match coin {
            Coin_ex2::Penny => 1,
            Coin_ex2::Nickle => 5,
            Coin_ex2::Dime => 10,
            Coin_ex2::Quarter(state) => {
                println!("State quarter from {state:?}!");
                25
            }

        }
    }

    // let .. else
    fn describe_state_quarter(coin: Coin) -> Option<String> {
        let Coin::Quarter(state) = coin else {
            return None;
        };
        if state.existed_in(1900) {
            Some(format!("{state:?} is pretty old for America"));
        }
        else {
            Some(format!("{state:?} is relatively new"));
        }
    }
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