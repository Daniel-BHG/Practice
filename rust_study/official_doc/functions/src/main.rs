fn main() {
    println!("Hello, world!");
    another_func(105);
    print_labeled(48, 'h');

    // expression macro
    let y = {
        let x = 3;
        x*3
    };
    println!("the value of y = {y}\n");

    // function w/ return value
    let x = five();
    println!("function w/ return value: {x}");

    let x = plus_one(31);
    println!("plus_one = 31 + 1 = {x}\n");
}

fn another_func(x: i32){
    println!("another func\n\tx = {x}\n");
}

fn print_labeled(value: i32, unit_label: char){
    println!("print_labeled\n\tvalue = {value}, unit_label = {unit_label}\n")
}

// specify the return type
fn five() -> i32 {
    5
}

fn plus_one(x: i32) -> i32 {
    x + 1
}