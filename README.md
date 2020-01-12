# Boggle Solver

Welcome to the Boggle Solver! A tool written in Python that can solve a boggle puzzle for you.

A Boggle is a puzzle where a 4x4 square block of letters is given and you are tasked to find valid words.

It looks like this:

`S` `A` `C` `E`  
`G` `Z` `E` `N`  
`E` `M` `K` `L`  
`M` `N` `O` `A`  

Solving the Boggle means that you have to find the hidden words by traversing the panel through the following rules:  
- Words can be constructed from the letters of sequentially adjacent cubes  
- Adjacent cubes are those horizontally, vertically, and diagonally neighboring.  
- Words must be at least two letters long.  
- Words may include singular and plural (or other derived forms) separately (eg. **player** and **players** as well as **play**, **playing**, **plays** and **played** and be all included if they can be constructed from the puzzle).  
- You may not use the same letter cube more than once per word.  

So for example in the above Boggle a few of the many valid words can be  
- ACE  
- LONE  
- ME  
- LAKE  

In order for the Boggle Solver to be able to provide you with the solutions, it needs to have a dictionary available under the name `dictionary` in the current directory.

A Greek dictionary is already included. Of course it doesn't include all the Greek words available but even with a small fraction of them (dictionary size at the time of writing is ~ 13k words) it is able to provide with numerous results for any given panel.

To run the solver for the given example, after making sure that the english `dictionary` file (or symlink) is in the same directory, you can run the following:  
```
python3 boggle.py SACEGZENEMKLMNOA
```

If you want to execute it in Greek, it will work with the already provided dictionary which you can expand at will.

For example  
```
python3 boggle.py ΑΣΛΕΝΣΙΑΛΣΕΝΗΩΟΜ
```

The output will be provided sorted by the ascending word length. The reason is that I believe this ordering makes more sense given you are more likely to get more points for bigger words. So the ordering by length is actually ordering by importance.
