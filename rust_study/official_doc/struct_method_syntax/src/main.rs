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

    // method syntax
    let rect_method_syntax = Rectangle_method_syntax{
        width: 30,
        height: 50,
    };
    println!("area of the rec is {}", rect_method_syntax.area());
}

// Tuple struct
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

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

// method syntax
struct Rectangle_method_syntax {
    width: u32,
    height: u32,
}

impl Rectangle_method_syntax {
    // if self exist, it's method
    fn area_m_s(&self) -> u32 {
        self.width * self.height
    }

    // it's a function in impl as it doesn't have self
    fn another_square_m_s(size: u32) -> Rectangle_method_syntax{
        Rectangle { width: size, height: size }
    }
}