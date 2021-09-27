var s = "afwf(abc)afe"
if (s.includes('(')) {
    print(reverseInParentheses(reverseOnce(s)));
} else {
    print(s);
}