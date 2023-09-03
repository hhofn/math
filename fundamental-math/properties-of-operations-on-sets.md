### Properties of Operations on Sets in Euler Diagrams

Euler diagrams are a graphical representation of sets and their relationships. They are similar to Venn diagrams but do not require all possible zones to be represented. In Euler diagrams, shapes (usually circles) represent sets, and the position of these shapes indicates the relationships between the sets.

#### Properties of Operations on Sets in Euler Diagrams:

1. **Union**: The union of two sets, A and B, denoted by \( A \cup B \), is the set of all elements that are in A, or in B, or in both.
2. **Intersection**: The intersection of two sets, A and B, denoted by \( A \cap B \), is the set of all elements that are both in A and in B.
3. **Difference**: The difference of two sets, A and B, denoted by \( A - B \), is the set of all elements that are in A but not in B.
4. **Complement**: The complement of a set A, denoted by \( A' \), is the set of all elements that are not in A.

Here's an example of an Euler diagram illustrating these properties:

![Euler Diagram](https://showme.redstarplugin.com/d/d:OQzg7Rq5)

#### C++ Code to Perform Set Operations:

```cpp
#include <iostream>
#include <set>

int main() {
    std::set<int> A = {1, 2, 3, 4};
    std::set<int> B = {3, 4, 5, 6};

    // Union
    std::set<int> unionSet;
    for (int a : A) unionSet.insert(a);
    for (int b : B) unionSet.insert(b);

    // Intersection
    std::set<int> intersectionSet;
    for (int a : A) {
        if (B.find(a) != B.end()) {
            intersectionSet.insert(a);
        }
    }

    // Difference (A - B)
    std::set<int> differenceSet = A;
    for (int b : B) {
        differenceSet.erase(b);
    }

    // Displaying the results
    std::cout << "A U B: ";
    for (int u : unionSet) std::cout << u << " ";
    std::cout << "\nA ∩ B: ";
    for (int i : intersectionSet) std::cout << i << " ";
    std::cout << "\nA - B: ";
    for (int d : differenceSet) std::cout << d << " ";
    std::cout << std::endl;

    return 0;
}
```

This C++ code demonstrates how to perform union, intersection, and difference operations on sets using the standard library's `set` container. The results are then displayed to the console.
