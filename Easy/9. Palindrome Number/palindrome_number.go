
func isPalindrome(x int) bool {

    var pow int = 1
    if x < 0{
        return false
    }
    for x >= pow{
        pow = pow * 10
    }
    pow /= 10
    for x > 0{
        if x % 10 != x / pow {
            return false
        }
        x = x - ((x/pow) * pow)
        x = x /10
        pow /=100
    }
    return true
}
