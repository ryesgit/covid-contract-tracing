# Contact Tracing App --- Le Finale!

Remember when you have to write onto a piece of paper so that people can keep track of you? Yeah... good times.

Somewhat related to that topic, behold: a digital Contact Tracing tool!

## How To Use It

### Clone This Repository

```
git clone https://github.com/ryesgit/covid-contract-tracing/tree/main
```

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the init file

```
python __init__.py
```

... and trace your contacts! Remember to always use back up!

## How It's Done

OOP! Here's some key features:

### Polymorphism!

The entry table inherits from the Table class, but it was morphed into displaying entry fields instead of label fields.

### Abstraction!

This happens for example with the search contacts form and contacts delegator (ContactsIO). 

Search contacts form need not know how contacts delegator gets the users if we want to get them by category. It just asks for data based on given metrics.

### Encapsulation!

Sometimes other widgets need to have access to a certain widget's window. Enter _get_table_frame of Table class which is used by protected member EntryTable!

Also, notice that a lot of instance variables can only be accessed privately (i.e., from within the same class only)

### Miscellaneous

Other features include:

- EntryTable does not break open/closed principle; widget types are [plugged](https://github.com/ryesgit/covid-contract-tracing/blob/487ea4a06f01205ad4735a5ec166e15f28a1f04a/components/SearchContactsForm.py#L79) into the class

- Scoping, this one's a fun implementation... see [on_submit](https://github.com/ryesgit/covid-contract-tracing/blob/487ea4a06f01205ad4735a5ec166e15f28a1f04a/components/SearchContactsForm.py#L79) lines here!

- Binded functions! Sometimes we want parameters of a function to be predetermined, but we don't want to use them yet. See the use of [partial](https://github.com/ryesgit/covid-contract-tracing/blob/487ea4a06f01205ad4735a5ec166e15f28a1f04a/components/SearchContactsForm.py#L74C8-L74C8). Pretty funky tool!

- Grid geometry management! Other geometry managements are cool and all, but they're quite hard to wrap around one's head, as [this article](https://tkdocs.com/tutorial/grid.html) says.