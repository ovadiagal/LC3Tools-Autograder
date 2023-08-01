# LC3Tools Autograding for Gradescope

Template for autograding LC-3 assembly programs with [LC3Tools](https://github.com/chiragsakhuja/lc3tools) and Gradescope's Docker images. Will likely be rebuilt into a [zucchini](https://github.com/zucchini/zucchini) grader down the line.

To run locally:

- Place any .asm files you wish to autograde inside the submission folder.
- Place the corresponding autograders inside source/lc3tools/test/tests. Make sure your assembly files and their corresponding autograder have the same name (i.e. linkedlist.cpp will run on linkedlist.asm). [Learn how to write an autograder using LC3Tools here.](https://github.com/chiragsakhuja/lc3tools/blob/master/docs/TEST.md)
- From the root directory, run `./source/run_autograder`
- Results will be available inside the results folder as a JSON. Check out [Gradescope's JSON formatting rules here.](https://gradescope-autograders.readthedocs.io/en/latest/specs/#output-format)

To add to a Gradescope image:

- Place any .asm files you wish to autograde inside the submission folder.
- Place the corresponding autograders inside source/lc3tools/test/tests. Make sure your assembly files and their corresponding autograder have the same name (i.e. linkedlist.cpp will run on linkedlist.asm). [Learn how to write an autograder using LC3Tools here.](https://github.com/chiragsakhuja/lc3tools/blob/master/docs/TEST.md).
- Zip all the files inside the source folder (zip the files themselves--not the folder. All the files needs to be at the root of the zip for this to work).
- Upload the zip to Gradescope and watch the magic happen! (Using the base Ubuntu 22.04 image on Gradescope)
