#include <string>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <stack>

using namespace std;



vector<string> split(string str, char delim)
{
    vector<string> parts;
    int previous = 0;
    int current = str.find(delim);

    while (current != string::npos)
    {
        parts.push_back(str.substr(previous, current-previous));

        previous = current+1;
        current = str.find(delim, previous);
    }
    parts.push_back(str.substr(previous, current-previous));

    return parts;
}



// class Node
// {
//     public:

//     int value;
//     Node* next;

//     Node(int valueX)
//     {
//         value = valueX;
//         next = NULL;
//     }
// };

// class Stack
// {
//     public:

//     Node* start;

//     Stack()
//     {
//         start = NULL;
//     }

//     void push(int newValue)
//     {
//         if (start == NULL)
//         {
//             start = new Node(newValue);
//         }
//         else
//         {
//             Node* newStart = new Node(newValue);
//             newStart->next = start;
//             start = newStart;
//         }
//     }

//     int pop()
//     {
//         int popValue;

//         if (start != NULL)
//         {
//             popValue = start->value;
//             start = start->next;
//         }

//         return popValue;
//     }

//     int top()
//     {
//         int topValue;
//         if (start != NULL) topValue = start->value;

//         return topValue;
//     }

//     bool isEmpty()
//     {
//         return start == NULL;
//     }
// };



int main()
{
    stack<long long int> s;

    // string commandsX;
    // getline(cin, commandsX);
    // int commands = atoi(commandsX.c_str());

    // for (int i = 0; i < commands; i++)
    // {
    //     string inputX;
    //     getline(cin, inputX);

    //     vector<string> input = split(inputX, ' ');

    //     if (input[0] == "1" && input.size() == 2) s.push(stoll(input[1]));
    //     else if (input[0] == "2" && input.size() == 1)
    //     {
    //         if (!s.empty()) s.pop();
    //     }
    //     else if (input[0] == "3" && input.size() == 1)
    //     {
    //         if (s.empty()) cout << "Empty!\n";
    //         else cout << s.top() << "\n";
    //     }
    // }

    int commands;
    scanf("%d", &commands);

    for (int i = 0; i < commands; i++)
    {
        int command;
        scanf("%d", &command);

        if (command == 1)
        {
            int newValue;
            scanf("%d", &newValue);

            s.push(newValue);
        }
        else if (command == 2)
        {
            if (!s.empty()) s.pop();
        }
        else if (command == 3)
        {
            if (s.empty()) printf("Empty!\n");
            else 
            {
                printf("%d", s.top());
                printf("\n");
            }
        }
    }
    
    return 0;
}