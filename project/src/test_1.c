#include "test_1.h"
#include "test_2.h"
#include "test_3.h"

int main(){
    Person person = {
        "alex",
        22
    };
    printf("My name is %s and I am %i years old!\n", person.name, person.age);
    Thing thing = {
        5
    };
    Data data = {
        10
    };
    printf("Thing: %i\n", thing.data);
    printf("Data: %i\n", data.data);
    return 0;
}