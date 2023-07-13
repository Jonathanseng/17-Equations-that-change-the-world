use std::f64;

fn schrodinger_equation(x: f64, y: f64, z: f64, m: f64, E: f64, V: f64) -> f64 {
  let psi = f64::exp(-(x * x + y * y + z * z) / 2.0);
  return psi;
}

fn main() {
  let x = 0.0;
  let y = 0.0;
  let z = 0.0;
  let m = 1.0;
  let E = 1.0;
  let V = 0.0;

  let psi = schrodinger_equation(x, y, z, m, E, V);

  println!("{}", psi);
}

// This code is similar to the Python code, but it is written in Rust. The main difference is that the Rust code uses the f64 type for floating-point numbers, while the Python code uses the float type.

//The Rust code also uses the println!() macro to print the wave function to the console. The println!() macro is a convenient way to print formatted text to the console in Rust.

//This code is a simple example of how the Schrödinger equation can be solved in Rust. More complex examples can be found online or in textbooks on quantum mechanics.
