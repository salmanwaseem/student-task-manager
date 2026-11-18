# Task title validation

The add operation strips surrounding whitespace and rejects titles that are blank after stripping. A ValueError tells users to enter a non-empty title. This guards the data model even when it is called outside the console.
