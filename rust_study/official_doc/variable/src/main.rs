const THREE_HOURS_IN_SECONDS: u32 = 60*60*3;

fn main() {
    // mut is for changing the value of the variable
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
    println!("The value of THREE_HOURS_IN_SECONDS is: {THREE_HOURS_IN_SECONDS}\n");

    // shadowing is for changing the type of the variable
    let x = 5;
    let x = x+1;
    { // temporary shadowing
        let x = x*2;
        println!("The value of x in the inner scope is: {x}");
    }
    println!("The value of x is: {x}"\n);

    // Data Types
    // need u32 for declaring the type
    let guess: u32 = "42".parse().expect("Not a number");

    // Floating-Point Types
    let x = 2.0; // Default f64
    let y: f32 = 3.0; // f32

    // Boolean type
    let t = true;
    let f: bool = false; // explicitly declare the type

    // Character type, 4-byte, more than ASCII
    let c = 'z';
    let z: char = 'ℤ'; // explicitly declare the type
    let heart_eyed_cat = '😻';

    // Compound Types
    // Tuple - cannot grow or shrink in size
    let tup_1: (i32, f64, u8) = (500, 6.4, 1);
    let tup_2 = (500, 6.4, 1);
    let (x, y, z) = tup_2;
    println!("tuple value: {x}, {y}, {z}");
    println!("tuple value: {0}, {1}, {2}", tup_1.0, tup_1.1, tup_1.2);

    // Array - all elements must have the same type and fixed size
    // flexible size type is Vec
    let a = [1,2,3,4,5];
    let a: [i32; 5] = [1,2,3,4,5];
    let a = [3; 5]; // [3,3,3,3,3]
    println!("array value: {0} {1} {2}", a[0], a[1], a[2]);
}
