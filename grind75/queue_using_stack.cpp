// 0ms solution

class MyQueue {
private:
    stack<int> data;
    stack<int> temp;
    void interchange(stack<int> *x1, stack<int> *x2){
        while(!x1->empty()){
            cout << x1->top() << endl;
            x2->push(x1->top());
            x1->pop();
        }
    }
public:
    MyQueue() {
    }
    
    void push(int x) {
        interchange(&data, &temp);
        data.push(x);
        interchange(&temp, &data);
    }
    
    int pop() {
        int res = data.top();
        data.pop();
        return res;
    }
    
    int peek() {
        return data.top();
    }
    
    bool empty() {
        return data.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */