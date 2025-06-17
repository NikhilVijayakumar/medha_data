## XIII. Entity Relationship Model (ER Model)

The Entity Relationship (ER) Model is a high-level conceptual data model diagram that provides a graphical representation of the entities, their attributes, and the relationships between them in a database. It's a blueprint used in the design phase of a database to understand and communicate the structure and requirements of the database.

**13. Entity Relationship Model (ER Model)**

* **Key Components:**

    * **Entities:** Real-world objects, concepts, or things about which data needs to be stored. In an ER diagram, entities are typically represented by rectangles.
        * **Example:** `Student`, `Course`, `Teacher`, `Order`, `Product`.

    * **Attributes:** Characteristics or properties of an entity. Attributes are represented by ovals connected to their respective entities.
        * **Types of Attributes:**
            * **Key Attribute:** An attribute (or a set of attributes) that uniquely identifies each instance of an entity. Often underlined in ER diagrams. (e.g., `StudentID` for the `Student` entity).
            * **Simple Attribute:** A single, atomic value (e.g., `StudentName`, `CourseCode`).
            * **Composite Attribute:** An attribute composed of multiple sub-attributes (e.g., `Address` can be composed of `Street`, `City`, `PostalCode`).
            * **Multi-valued Attribute:** An attribute that can have multiple values for a single entity instance (e.g., `Skills` of a `Teacher`). These are sometimes represented by double ovals.
            * **Derived Attribute:** An attribute whose value can be calculated from other attributes (e.g., `Age` can be derived from `DateOfBirth`). These are sometimes represented by dashed ovals.

    * **Relationships:** Associations or connections between two or more entities. Relationships are represented by diamond shapes connected to the entities they relate. The name of the relationship is usually written inside the diamond.
        * **Example:** A `Student` `ENROLLS IN` a `Course`. A `Teacher` `TEACHES` a `Course`.

    * **Primary Keys:** Attributes that uniquely identify each instance of an entity. They are crucial for establishing relationships between tables in the relational database schema derived from the ER model.

    * **Cardinality:** Specifies the number of instances of one entity that can be associated with the number of instances of another entity participating in a relationship. Cardinality constraints are placed on the lines connecting entities to the relationship diamond. Common types include:
        * **One-to-One (1:1):** Each instance of entity A is associated with at most one instance of entity B, and each instance of entity B is associated with at most one instance of entity A.
            * **Example:** A `Person` has one `Passport`.
        * **One-to-Many (1:M):** One instance of entity A can be associated with zero, one, or many instances of entity B, but each instance of entity B is associated with exactly one instance of entity A.
            * **Example:** A `Teacher` `TEACHES` many `Students`. A `Department` has many `Employees`.
        * **Many-to-One (M:1):** Multiple instances of entity A can be associated with one instance of entity B, but each instance of entity B is associated with multiple instances of entity A. This is the same relationship as One-to-Many viewed from the other direction.
            * **Example:** Many `Students` are enrolled in one `Course`. Many `Employees` belong to one `Department`.
        * **Many-to-Many (M:N):** Multiple instances of entity A can be associated with multiple instances of entity B, and vice versa. These relationships often require an intermediary (junction) entity to be resolved into two one-to-many relationships in the relational database schema.
            * **Example:** `Students` `ENROLL IN` many `Courses`, and `Courses` have many `Students`. This would typically be resolved with an `Enrollment` entity having foreign keys to both `Students` and `Courses`.

* **Degree of Relationship:** Refers to the number of entity types involved in a relationship.

    * **Unary (Degree 1):** A relationship exists between instances of the same entity type. Also known as a recursive relationship.
        * **Example:** An `Employee` `MANAGES` another `Employee`.
    * **Binary (Degree 2):** A relationship exists between instances of two different entity types. (Most common type).
        * **Example:** A `Student` `ENROLLS IN` a `Course`.
    * **Ternary (Degree 3):** A relationship involves three different entity types simultaneously.
        * **Example:** A `Doctor` `PRESCRIBES` a `Medicine` to a `Patient` (the relationship depends on all three entities).
    * **Higher-Degree:** Relationships involving more than three entity types are less common and can often be decomposed into multiple binary relationships.

The ER Model provides a crucial step in the database design process. By visually representing the entities, their attributes, and the relationships between them, it helps stakeholders understand the data requirements and forms the basis for translating the conceptual model into a logical (relational schema) and then a physical database design. The cardinality and degree of relationships are particularly important for determining how tables will be structured and related using primary and foreign keys in the relational database.