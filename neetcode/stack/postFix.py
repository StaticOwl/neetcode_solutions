#Also I didn't wanna use the traditional switch case type approach. So, I used eval() function to evaluate the
#expression. eval() function takes a string as an argument and evaluates it as a python expression. So, I used
#format() function to format the string and then passed it to eval() function. This is a very good example of
#using eval() function.
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i in ('+', '-', '*', '/'):
                a=stack.pop()
                b=stack.pop()
                stack.append(int(eval("{}{}{}".format(float(b),i,a))))
            else:
                stack.append(i)
            print(stack)

        return int(stack.pop())
