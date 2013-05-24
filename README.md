Unicorn
=======
An interpreted language built in python and designed for complete beginners
(https://github.com/gulnara/unicorn)

Summary
-------
* Syntax of the language is constructed in a way that “humanizes” general programming principles found in other languages. 
* Lexer is built with 47 regular expressions.
* Parser is constructed using Pratt’s algorithm, which associates semantics with tokens instead of grammar rules; it uses left and right binding powers to handle precedence levels and makes tokens the nodes of the tree.
* Interpretation is handled via evaluation functions inside each class of the tokens.
* I wrote a simple guessing game using Unicorn to showcase current capabilities of the language, such as variable assignment, user input, random number generation, conditional statements and loops.
* Unicorn was built in 4 weeks. 

Lexing
------
The main body of the lexer [starts here](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L447-L450), matching tokens using regular expressions and emitting token objects.

Parsing
-------
Parsing is done as a combination of recursive descent and Pratt's parser. Evaluating statements is done as standard recursive descent with the [statement function](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L486-L496). It first checks tokens for their class type. If the token is of StatementToken class, then the std function will be invoked. Otherwise, the statement will be parsed as an expression with the [expression function](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L470-L482).

The expression function is the core of the Pratt parser. The current token is held in global variable 'token'. The [next function](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L455-L466) advances the token stream to the next token. It will fetch the next token until it runs into FinalToken, which signifies the end of the program. 

In Pratt's algorithm, the nud function signifies 'null denotation' and led function signifies 'left denotation'. Additionally, an lbp (left binding power) attribute is assigned to each token, which dictate the precedence of the tokens. The combination of these three things allow the parser to consume expressions by evaluating each token in terms of how strongly it binds to the token immediately following it.

The Pratt parser is used for all tokens that are not children of the StatementToken class. For those tokens we use the std which contains the parsing rules for any statement that begins with that particular token type. For an example see the [LoopToken](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L317-L333).

The final AST is assembled using the token objects as nodes. Not all tokens make it into the AST, many are consumed and discarded as part of the parsing process.

Evaluation
----------
Evaluation is done recursively by executing each token's eval method starting from the top token node in the AST. For examples, see the eval methods of [LoopToken](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L334-L340) and [AssignToken](https://github.com/gulnara/unicorn/blob/master/unicorn_tokenizer.py#L310-L311).

Sample Guessing Game
--------------------
To showcase the capabilities of the code, including looping and conditional execution, I wrote a simple guessing game, which you can find in [guessing_game.uni](https://github.com/gulnara/unicorn/blob/master/guessing_game.uni) . 

Future Work
-----------
There is still a lot of work to be done to bring this language to "completion", including refactoring and optimizing the existing code. Currently, there is a flaw in the way 'break' statements are evaluated: if a loop is broken early, the remainder of the body is executed anyway, it simply prevents it from starting the next iteration.
