# Letters
Letters is an esoteric programming language for extracting hidden messages from letters/emails (it can also do addition with natural numbers). A number of sample programs are given in .txt files.


## Usage

a file written in letters can be executed using letters.py
>python3 letters.py (file_name)


## Syntax

The general format of a Letters program follows that of the standard format of an email/letter. There is an introduction, a series of one or more statements, and a sign off or outro. Many elements of the program can be padded out with **words** to make the language more natural. **words** are just strings of alpha numeric characters (and the apostrophe) seperated by spaces.

**Introduction:**

The format of the introduction is a greeting (such as Dear, Hi, or Hello) followed by some **words** (usually someones name), a comma, and one or more new lines.
```
Dear some name or something,

```

**Statements:**

Statements represent sentances within the body of a letter/email. Statements can either be **filler** or **commands**. **filler** statements are just sentances that don't do anything (they can be used to pad out the email with more natural language). 

**Outro:**

The format of the outro is some signing off words (such as Sincerely, Thanks, or Regards) followed by a new line and some **words** (usually the name of the writer).
```
Thanks,
Tim
```
It is also possible to sign off with just the ending **words**.
```
-name of the writer or something
```
