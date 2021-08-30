class MinStack {
    LinkedList<Integer> minStack;
    LinkedList<Integer> myStack;
    public MinStack() {
        minStack=new LinkedList<>();
        myStack=new LinkedList<>();
    }
    
    public void push(int val) {
        myStack.addLast(val);
        if (minStack.isEmpty()){
            minStack.addLast(val);
        }else{
            if (minStack.getLast()>val){
                minStack.addLast(val);
            }else{
                minStack.addLast(minStack.getLast());
            }
        }
    }
    
    public void pop() {
        myStack.removeLast();
        minStack.removeLast();
    }
    
    public int top() {
        return myStack.getLast();
     
    }
    
    public int getMin() {
        return minStack.getLast();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */