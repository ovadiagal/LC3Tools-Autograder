# Primitive LC3Tools Autograding for Gradescope

Template for autograding LC-3 assembly programs with [LC3Tools](https://github.com/chiragsakhuja/lc3tools) and Gradescope's Docker images. Will likely be rebuilt into a [zucchini](https://github.com/zucchini/zucchini) grader down the line.
[Learn how to write an autograder using LC3Tools here.](https://github.com/chiragsakhuja/lc3tools/blob/master/docs/TEST.md)

To run locally:

- Place any .asm files you wish to autograde inside the `submission` folder.
- Place the corresponding autograders inside `source/lc3tools/test/tests`. Make sure your assembly files and their corresponding autograder have the same name (i.e. `linkedlist.cpp` will run on `linkedlist.asm`).
- From the root directory, run `./source/run_autograder`
- Results will be available inside the `results` folder as a JSON. Check out [Gradescope's JSON formatting rules here.](https://gradescope-autograders.readthedocs.io/en/latest/specs/#output-format)

To add to a Gradescope image:

- Place your autograders inside `source/lc3tools/test/tests`. Make sure the files you've provided students and the corresponding autograders have the same name (i.e. `linkedlist.cpp` will run on `linkedlist.asm`).
- Zip up everything the `source` folder as shown in the image below (zip the files themselves--not the folder. Everything needs to be at the root of the zip for this to work!).
- Upload the zip to Gradescope and watch the magic happen! (Using the base Ubuntu 22.04 image on Gradescope)
<img width="350" alt="Screenshot 2023-08-02 at 3 32 28 PM" src="https://github.com/ovadiagal/LC3Tools-Autograder/assets/102482702/36f47c2b-6e2c-42e5-b760-9d3039f5f32e">
