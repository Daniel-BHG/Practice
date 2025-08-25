fn main() {
    // specify the type
    let v: Vec<i32> = Vec::new();
    let v = vec![1,2,3];
    
    // non-specified vector, but need the element
    let mut v_update = Vec::new();
    v_update.push(5);
    v_update.push(6);

    let v_read_elem = vec![1,2,3,4,5];
    // & is not address, but borrowing 참조
    /*
    If we declare the vector with Vec<T>, rust will infer the type
    Default: integer -> i32, float -> f64, 'c' -> char, "c" -> string
     */
    let third: &i32 = &v[2];
    println!("third element is {third}");

    let third: Option<&i32> = v.get(2);
    match third {
        Some(third) => println!("third element is {third}");
        None => println!("no third elem");
    }
}
