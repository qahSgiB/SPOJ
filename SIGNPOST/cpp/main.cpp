#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

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

bool isWord(string str) {
    bool isWordX = true;

    if (str.length() == 0) isWordX = false;
    else
    {
        for (string::iterator chr = str.begin(); chr != str.end(); ++chr)
        {
            if (!isalpha(*chr)) isWordX = false;
            if (!isWordX) break;
        }
    }

    return isWordX;
}



int main() {
    vector<string> lines;

    string newLine;
    while (getline(cin, newLine)) {
        lines.push_back(newLine);
    }

    // string newLine;
    // getline(cin, newLine);
    // lines.push_back(newLine);

    for (vector<string>::iterator lineP = lines.begin(); lineP != lines.end(); ++lineP)
    {
        string line = *lineP;

        bool leftOk = false;
        string left;
        bool rightOk = false;
        string right;
        
        vector<string> parts = split(line, '.');

        if (parts.size() == 3)
        {
            if (parts[2] == "")
            {
                vector<string> leftParts = split(parts[0], ' ');
                vector<string> rightParts = split(parts[1], ' ');

                if (leftParts.size() == 3)
                {
                    if (leftParts[0] == "Left" && leftParts[1] == "to")
                    {
                        string leftX = leftParts[2];

                        if (isWord(leftX))
                        {
                            left = leftX;
                            leftOk = true;
                        }
                    }
                }

                if (rightParts.size() == 4)
                {
                    if (rightParts[0] == "" && rightParts[1] == "Right" && rightParts[2] == "to")
                    {
                        string rightX = rightParts[3];

                        if (isWord(rightX))
                        {
                            right = rightX;
                            rightOk = true;
                        }
                    }
                }
            }
        }

        if (leftOk && rightOk)
        {
            if (left == "dragon" && right != "dragon") cout << "Right, to the "+right+"!\n";
            else if (right == "dragon" && left != "dragon") cout << "Left, to the "+left+"!\n";
        }
    }
}