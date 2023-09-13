import (
    "strconv"
)


func addBinary(a string, b string) string {
    result := ""
    diffSize := len(a) - len(b) // a > b
    if diffSize < 0{
        diffSize *= -1
        a,b = b,a
    }
    for i:= 0 ; i < diffSize; i++{
        b = "0" + b
    }
    var num1 int
    var num2 int
    prev := 0
    for i := len(a) -1; i >= 0; i-- {
        num1,_ = strconv.Atoi(a[i:i+1])
        num2,_ = strconv.Atoi(b[i:i+1])
        result = fmt.Sprintf("%d",((num1 + num2 + prev)%2)) + result
        prev = (num1 + num2 + prev)/2
    }

    if prev == 1{
        result = fmt.Sprintf("%d", prev) + result
    } 
    return result
}
