---
author: Micha
author_link: http://github.com/mynameisfiber
date: "2015-04-23T15:16:56Z"
feature: true
preview_image: http://i.imgur.com/OodCK0c.png
redirect_from:
- /post/117173339298/bytecode-hacking-for-great-justice
tags:
- code
- python
- bytecode
- optimization
title: Bytecode Hacking for Great Justice
aliases:
  - /2015/04/23/bytecode-hacking-for-great-justice.html
---

<p><em>DO NOT TRY THIS AT HOME! NO PYTHONS WERE HURT IN THE CREATION OF THIS BLOG POST!</em></p>
<p>Check out the code at code at <a href="http://github.com/mynameisfiber/pytailcall">github.com/mynameisfiber/pytailcall</a></p>
<p>As an exercise into learning more about python 2.7 bytecode, I wanted to implement the thing that pythonistas <a href="http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html">love to hate</a> - tail call optimization! This isn&rsquo;t <a href="http://www.teamrubber.com/blog/python-tail-optimisation-using-byteplay/">novel</a> at all, but I chose to implement this only using the standard library so that I could understand more about generating and modifying bytecode. As a result, I&rsquo;m sure there are <em>many</em> edge cases that I don&rsquo;t consider so please, keep your sys-ops sane and <em>do not use this code in production</em>. <a href="https://github.com/mynameisfiber/pytailcall/">In the end</a>, even though the code is fun it is a filthy hack that shouldn&rsquo;t be used in production code and should never be considered to make it&rsquo;s way into the python source. One point I really like on <a href="http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html">Guido&rsquo;s blog post</a> about this issue is tail recursion optimization ruins the stack traces and detracts from python&rsquo;s ability to debug easily.</p>
<p>Tail calls are when a function is recursing and returns simply on a function call to itself. This is different than normal recursion where multiple things can be happening on our recursed return statement. So, for example, this is tail recursion,</p>

```python
def factorial(N, result=1):
    if N == 1:
        return result
    return factorial(N-1, N*result)
```
While this is not,

```python
def factorial(N):
    if N == 1:
        return 1
    return N * factorial(N-1)
```

<p>So we can see that normal recursion uses the return register in order to maintain the state of the calculation. By contrast, tail recursion uses a function parameter. This is made particularly simple in python because you can have keyword arguments with default values to initialize the calculation.</p>
<p>The thing that makes tail calls particularly useful is the ability to optimize them. Generally when a function gets called, the system must set up a function stack in memory that maintains the state of the function, including local variables and code pointers, so that the function can go on its merry way. However, when we do a tail recursion we are trying to enter the same function stack that we are already in, just with changes to the values of the arguments! This can be quickly optimized by never creating the new function stack and instead just modifying the argument values and starting the function from the beginning!</p>
<p>One way of doing this is manually unravelling the recursion. For our example above, the factorial would become,</p>

```python
def factorial(N, result=1):
    while True:
        if N == 1:
            return result
        N, result = N-1, N*result
```

<p>Not only will this speed up our code, but we also don&rsquo;t have to worry about those pesky <a href="https://docs.python.org/2/library/sys.html#sys.setrecursionlimit">recursion limits</a> that python imposes on us. Furthermore, the transformation is quite simple. All we did was add a <code>while True:</code> to the beginning of the function and change any tail calls with changes to the argument variables.</p>
<p>There are a whole host of methods to do this automatically (<a href="http://tomforb.es/adding-tail-call-optimization-to-python">partial functions</a>, <a href="http://lambda-the-ultimate.org/node/1331">exceptions</a>, etc., but I thought it would be fun to do this by re-writing the bytecode of the function itself. Let&rsquo;s start by looking at the actual bytecode of the <code>factorial</code> function using the <code>dis</code> module from the standard library.</p>

```
>>> dis.dis(factorial)
# bytecode                                             # relevant python
# -----------------------------------------------------#---------------------
  2           0 LOAD_FAST                0 (N)         # if N == 1:
              3 LOAD_CONST               1 (1)         #
              6 COMPARE_OP               2 (==)        #
              9 POP_JUMP_IF_FALSE       16             #
                                                       #
  3          12 LOAD_FAST               1 (result)     #    return result
             15 RETURN_VALUE                           #
                                                       #
  4     >>   16 LOAD_GLOBAL              0 (factorial) # return factorial(N-1, N*result)
             19 LOAD_FAST                0 (N)         #
             22 LOAD_CONST               1 (1)         #
             25 BINARY_SUBTRACT                        #
             26 LOAD_FAST                0 (N)         #
             29 LOAD_FAST                1 (result)    #
             32 BINARY_MULTIPLY                        #
             33 CALL_FUNCTION            2             #
             36 RETURN_VALUE                           #
```

<p>We can see the full structure of our function in the bytecode. First we load up <code>N</code> and the constant <code>1</code> and compare them using the <code>COMPARE_OP</code> bytecode. If the result if false, we jump to line 16 and if not we load the variable <code>result</code> into the stack and return it. On line 16, we first load the reference to the function named <code>factorial</code> (which happens to be the same function we&rsquo;re in!) and start building up the arguments. First we load up <code>N</code> and <code>1</code> and call <code>BINARY_SUBTRACT</code> which will leave the value of <code>N-1</code> on the stack. Then we load up <code>N</code> and <code>result</code> and multiply them with <code>BINARY_MULTIPLY</code> which will push the value of <code>N-1</code> onto the stack. By calling the <code>CALL_FUNCTION</code> bytecode (with the argument <code>2</code> indicating that there are two arguments to the function), python can go out and start running the function in another context until it returns and we can call <code>RETURN_VALUE</code> on line 36 to return whatever is left in the stack. This may seem like a convoluted way of approaching how a function works (although it <a href="http://shop.oreilly.com/product/0636920028963.do">has its uses</a>!), but after a while spent looking at <a href="http://unpyc.sourceforge.net/Opcodes.html">opcodes</a> this starts to make just as much sense as python itself!</p>
<p>In an ideal world, what would we want this bytecode to look like? Looking up the references on <code>JUMP_ABSOLUTE</code>, we can rewrite the above bytecode to be,</p>

```
  2     >>    0 LOAD_FAST                0 (N)
              3 LOAD_CONST               1 (1)
              6 COMPARE_OP               2 (==)
              9 POP_JUMP_IF_FALSE       16

  3          12 LOAD_FAST               1 (result)
             15 RETURN_VALUE

  4     >>   16 LOAD_FAST                0 (N)
             19 LOAD_CONST               1 (1)
             22 BINARY_SUBTRACT
             23 LOAD_FAST                0 (N)
             26 LOAD_FAST                1 (result)
             29 BINARY_MULTIPLY
             30 STORE_FAST               1 (result)
             33 STORE_FAST               0 (N)
             36 JUMP_ABSOLUTE            0
```

<p>The differences here start at line 16. Instead of loading a reference to the recursed function, we immediately start filling up the stack with what <em>were</em> the arguments to the function. Then, once our arguments have been computed, instead of doing a <code>CALL_FUNCTION</code>, we start running a sequence of <code>STORE_FAST</code> to pop the calculated arguments off the stack and into the actual argument variables. Now that the arguments have been modified, we can call <code>JUMP_ABSOLUTE</code> with an argument of <code>0</code> in order to jump back to the beginning of the function and starting again. This last aspect, the <code>JUMP_ABSOLUTE</code> back to the beginning of the function as oppose to setting up a while loop, is one of the reasons this function is faster than the manual unrolling of the recursion we did above; we don&rsquo;t need to calculate the conditions of the loop or do any modifications to our state, we simply start processing opcodes at line 0 again.</p>
<p>This may seem simple, but there are many corner cases that will get you (and in fact got me in the hours of <code>SystemError</code> exceptions I wrestled with). First of all, if the recursive return is already within what python calls a block (ie: a loop or a try..except..finally block), we need to call the <code>POP_BLOCK</code> opcode the right amount of times before our <code>JUMP_ABSOLUTE</code> so that we properly terminate any setup those sections need.</p>
<p>Another problem, and probably much more annoying than the block counts, is that of changing the size and thus the addresses of the bytecodes. When bytecode is represented, it is simply a list of unsigned four-bit integers. Some of these integers represent jumps to other points in the list, and it refers to those other points by either relative offsets (e.g., jump five integers to the right) or by absolute addresses (e.g., jump to the tenth integer). In order to make sure these jumps go to the correct place after we modify the bytecode, we must keep a list of what we added (and where) and, once our editing is done, go back through and modify any addresses to again point to the correct place.</p>
<p>Once all these problems are solved, we are left with a <a href="https://github.com/mynameisfiber/pytailcall/blob/master/pytailcall/internal_loop.py#L77">general decorator</a> to transform all of our tail recursion into the iterative versions! And this is indeed much faster. Looking at the benchmark supplied with <a href="https://github.com/mynameisfiber/pytailcall/">pytailcall</a>, we can see that we reduce the overhead of recursion (by eliminating it) and are able to recurse much more than we were previously able to.</p>

<a href="http://i.imgur.com/OodCK0c.png"><img src="http://i.imgur.com/OodCK0c.png" alt="pytailcall benchmarks"/></a>

<p>In the <a href="https://github.com/mynameisfiber/pytailcall/blob/master/pytailcall/examples.py">benchmark</a> above, <code>native</code> is the original function (note that native python could not complete all of the benchmarks due to maximum recursion errors). <code>partial_func</code> is a trick which wraps the function in a partial and changes it&rsquo;s internal reference to itself. <code>return_tuple</code> is another bytecode hack that changes the recursion into a specialized return statement that triggers another call to the function. Finally, <code>internal_loop</code> is the bytecode hack described above.</p>
<p>So, by committing this ungodly sin against all things python stands for, we can get a 33% speedup over python tail recursed code! In general though, this was a great exercise in learning much more about how python bytecode works and the underlying structure of a function. While this sort of bytecode hacking is exactly that, a hack, being able to read bytecode and understand the output of <code>dis.dis</code> is incredibly useful when optimizing python code for actual production systems. If you want to know more about <em>that</em> aspect of the optimization, and other more rigorous methods of optimization, check out <a href="http://shop.oreilly.com/product/0636920028963.do">High Performance Python</a>.</p>

<p>-Micha</p>
