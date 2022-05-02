# Letters
Letters is an esoteric programming language for extracting hidden messages from letters/emails (it can also do addition with natural numbers). A number of sample programs are given in .txt files.


## Usage

a file written in Letters can be executed using letters.py
>python3 letters.py (file_name)


## Syntax

The general format of a Letters program follows that of the standard format of an email/letter. There is an introduction, a series of one or more statements, and an outro. Many elements of the program can be padded out with **words** to make the language more natural. **words** are just strings of alpha numeric characters (and the apostrophe) seperated by spaces.

#### Introduction

The format of the introduction is a greeting (such as Dear, Hi, or Hello) followed by some **words** (usually someones name), a comma, and one or more new lines.
```
Dear some name or something,

```

#### Statements

Statements represent sentences within the body of a letter/email. Statements can be seperated by new line characters to form paragraphs. Statements can either be **filler** or **commands**.

**filler** statements are just sentences that don't do anything (they can be used to pad out the email with more natural language). **filler** sentences just consist of **words** that do not include any key words used by **commands** followed by a sentence terminal {. ? ! ,} (commas are included). In certain cases **filler** can include key words (for example, you can include "the" or "for" if there are no command keywords in previous sentences), however in most cases it is best to avoid them when writing **filler**.
```
These are filler sentences. They don't include any key words.
```

**Commands:**

**commands** contain one or more sentences that specify the operation to be executed and its arguments (if needed) using certain key words within the **middle** of a sentence. The general structure of a **command** is a sentence with a command key word followed by a series of **arg**s. An **arg** is a sentence containing the "the" or "of" key word. The data of the **arg** is hidden in the words around the key word.

**print**
>keyword: " day "
>
>takes one or more args
>
>args after the first arg can be seperated by filler (print arg filler filler arg filler arg)

This command will print out one word from each **arg**. The sentence immediatly after the command must be an **arg**. The word to be printed is the nth word after the key word in the **arg** where 'n' is the current **offset** (default is 0 so first word after the keyword).
```
This statement will print Hello World day yup. This sentence must be an arg the Hello. This sentence can be filler. This is the World second arg. 
```

**char_print**
>keyword: " with "
>
>takes one or more args
>
>args after the first arg can be seperated by filler (char_print arg filler filler arg filler arg)

This command will print out one letter from each **arg**. The sentence immediatly after the command must be an **arg**. The letter to be printed is the first letter of the nth word after the key word in the **arg** where 'n' is the current **offset** (default is 0 so first word after the keyword).

**offset_up**
>keyword: " about "
>
>takes no args

This command will increase the offset by 1. (currently out of bound offsets are not correctly handled)

**offset_down**
>keyword: " out "
>
>takes no args

This command will decrease the offset by 1. (currently negative offsets are not correctly handled)

**add**
>keyword: " up "
>
>takes one or more args
>
>args after the first arg can be seperated by filler (add arg filler filler arg filler arg)

This command will add up a number of integers and print the total. In each **arg**, all integers found within the words after the key word will be used. 

#### Outro

The format of the outro is some signing off words (such as Sincerely, Thanks, or Regards) followed by a new line and some **words** (usually the name of the writer).
```
Thanks,
Tim
```
It is also possible to sign off with just the ending **words**.
```
-name of the writer or something
```
