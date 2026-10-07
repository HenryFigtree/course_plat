"""
Resources repo

Contains database operations for resources (links, sections, files)
"""
class ResourceRepository:
    def __init__(self, db):
        self.db = db

    def get_resources(self, module_id):
        rows = self.db.execute(
            """
            SELECT
                r.id,
                r.resource_type,
                l.link_text,
                l.url,
                f.file_name,
                f.file_path,
                s.title,
                s.content
            FROM resources r
            LEFT JOIN links l
                ON l.resource_id = r.id
            LEFT JOIN files f
                ON f.resource_id = r.id
            LEFT JOIN sections s
                ON s.resource_id = r.id
            WHERE r.module_id = ?
            ORDER BY COALESCE(l.position, f.position, s.position)
            """,
            (module_id,)
        ).fetchall()

        resources = Resources()

        for row in rows:
            if row["resource_type"] == "link":
                resource = Link(
                    row["link_text"],
                    row["url"]
                )

            elif row["resource_type"] == "file":
                resource = File(
                    row["file_name"],
                    row["file_path"]
                )

            elif row["resource_type"] == "section":
                resource = Section(
                    row["title"],
                    row["content"]
                )

            resources.add(resource)

        return resources

    def add_resource(self, module_id, resource):
        resource_type = ""

        if isinstance(resource, Link):
            resource_type = "link"

        elif isinstance(resource, File):
            resource_type = "file"

        elif isinstance(resource, Section):
            resource_type = "section"

        cursor = self.db.execute(
            """
            INSERT INTO resources (module_id, resource_type)
            VALUES (?, ?)
            """,
            (module_id, resource_type)
        )

        resource_id = cursor.lastrowid

        if isinstance(resource, Link):
            self.db.execute(
                """
                INSERT INTO links
                (resource_id, url, link_text)
                VALUES (?, ?, ?)
                """,
                (
                    resource_id,
                    resource.url,
                    resource.text
                )
            )

        elif isinstance(resource, File):
            self.db.execute(
                """
                INSERT INTO files
                (resource_id, file_name, file_path)
                VALUES (?, ?, ?)
                """,
                (
                    resource_id,
                    resource.filename,
                    resource.path
                )
            )

        elif isinstance(resource, Section):
            self.db.execute(
                """
                INSERT INTO sections
                (resource_id, title, content)
                VALUES (?, ?, ?)
                """,
                (
                    resource_id,
                    resource.title,
                    resource.body
                )
            )
