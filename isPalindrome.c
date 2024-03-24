bool isPalindrome(int x){
    if (x < 0) return false;

    unsigned int rev = 0;
    int num = x;

    while (num != 0){
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev == x;
}
