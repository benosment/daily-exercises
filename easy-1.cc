#include <iostream>
#include <fstream>

// create a program that will ask the users name, age, and reddit
// username. have it tell them the information back, in the format:

// your name is (blank), you are (blank) years old, and your username is
// (blank)

// for extra credit, have the program log this information in a file to
// be accessed later.

using namespace std;

int main() {
  string name, username;
  int age;
  ofstream outfile;

  cout << "What is your name? ";
  cin >> name;
  cout << "What is your age? ";
  cin >> age;
  cout << "What is your reddit username? ";
  cin >> username;

  cout << "your name is " << name << ", you are " << age << " years old and your username is " << username << endl;

  outfile.open("easy-1-cc.txt");
  outfile << "your name is " << name << ", you are " << age << " years old and your username is " << username << endl;
  outfile.close();

}
