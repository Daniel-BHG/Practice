fn main() {
    let number = 3;

    if number < 5 {
        println!("True\n");
    } else {
        println!("False\n");
    }

    println!("to_bool = {}\n", to_bool(number));

    let condition = true;
    let number = if condition {5} else {6};
    println!("condition number = {number}");
}

fn to_bool(x: i8) -> bool {
    x < 5
}
