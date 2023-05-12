gifts=[
    "A partridge in a pear tree.",
    "Two turtle doves",
    "Three French hens",
    "Four calling birds",
    "Five golden rings",
    "Six geese a-laying",
    "Seven swans a-swimming",
    "Eight maids a-milking",
    "Nine ladies dancing",
    "Ten lords a-leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming"
]
days=["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
for i in range(12):
    print(f"On the {days[i]} day of Christmas\nmy true love sent to me:")
    for j in range(i, -1, -1):
        if j==0 and i !=0:
            print("And", end=" ")
        print(gifts[j])
    print()