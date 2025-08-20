#[derive(Debug)]

fn main() {
    let mut user1 = User {
        active: true,
        username: String::from("someusername123"),
        email: String::from("someuser@example.com"),
        sing_in_count: 1,
    };
    user1.email = String::from("another@example.com");

    // struct update syntax
    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sing_in_count: user1.sing_in_count,
    };

    let user3 = User {
        email: String::from("another@example.com"),
        ..user1 // same components with user1
    };

    // tuple type struct
    let black = Color(0,0,0);
    let origin = Point(0,0,0);

    // unit-like structs
    let subject = AlwaysEqual;

    // -------------------------------------------------------------------------
    // examples using struct
    // rectangle area ex with Tuples
    let rect1 = (30, 50);
    println!("retangle area: {}", area(rect1));

    // rectangle area ex with struct
    let rect2 = Rectangle { // immutable
        width: 30,
        height: 50,
    };
    println!("rectangle area: {}", area_struct(&rect2)); // & type - because immutable
}

struct User {
    active: bool,
    username: String,
    email: String,
    sing_in_count: u64,
}

fn build_user(email: String, username: String) -> User {
    User {
        active: true,
        username: username,
        email: email,
        sing_in_count: 1,
    }
}

// Tuple struct
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

// unit-like structs
struct AlwaysEqual;

// rectangle area with Tuples
fn area(dimensions: (u32, u32)) -> u32 {
    dimensions.0 * dimensions.1
}

// rectangle area ex with struct
struct Rectangle {
    width: u32,
    height: u32,
}

fn area_struct(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}