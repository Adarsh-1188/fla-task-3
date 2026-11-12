ARITHMETIC_GRAMMAR = {
    "E": ["T E'"], "E'": ["+ T E'", "epsilon"],
    "T": ["F T'"], "T'": ["* F T'", "epsilon"],
    "F": ["( E )", "id"],
}
PARENTHESIS_GRAMMAR = {"S": ["( S ) S", "epsilon"]}
PALINDROME_GRAMMAR = {"S": ["a S a", "b S b", "a", "b", "epsilon"]}
