fn main() {
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter*2;
        }
    };
    println!("Result = {result}\n");

    // loop statement
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }
        count += 1;
    }
    println!("final count = {count}\n");

    // loop while
    let mut num_while = 3;
    while num_while != 0 {
        println!("{num_while}");
        num_while -= 1;
    }
    println!("LIFTOFF!!\n");

    // for loop in array
    let a = [10, 20, 30, 40, 50];
    for element in a {
        println!("the value = {element}");
    }
    println!("\n");

    for number in (1..4).rev() {
        println!("reverse for loop {number}");
    }
}
