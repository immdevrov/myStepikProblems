class StackItem {
  constructor (item, next = null) {
    this.next = next;
    this.value = item;
  }

  toString (f) {
    if (f && typeof f === 'function')
      return `${f(this.value)}`
    return `${this.value}`
  }
}

class Stack {
  constructor () {
    this.head = null;
    this._length = 0;
  }

  push (item) {
    const newItem = new StackItem(item, this.head);
    this.head = newItem;
    this._length++;
  }

  pop () {
    const newHead = this.head.next;
    const popped = this.head;
    this.head = newHead;
    this._length--;
    return popped;
  }

  top () {
    return this.head;
  }

  isEmpty () {
    return this._length === 0;
  }

  get length () {
    return this._length;
  }

  toArray () {
    const watchedList = this;
    const arr = [];
    while (!watchedList.isEmpty()) {
      arr.push(watchedList.pop().toString());
    };
    return arr;
  }
}


function isValid (seq) {
  const stack = new Stack();
  for (let char of seq) {
    if ('(['.includes(char)) {
      stack.push(char);
    } else {
      if (stack.isEmpty()) { return false; };
      const top = stack.pop().value;
      if ((top === '[' && char !== ']') || ((top === '(' && char !== ')'))) {
        return false;
      }
    }
  }
  return stack.isEmpty();
}

console.log(isValid('()[()]()()[]'));
