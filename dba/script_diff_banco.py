import cx_Oracle
import difflib


def get_procedure_source(conn, procedure_name):
    """
    Obtém o código-fonte de uma procedure específica do banco de dados Oracle.
    """
    query = """
        SELECT TEXT
        FROM ALL_SOURCE
        WHERE NAME = :dbaps.prc
        AND TYPE = 'PROCEDURE'
        ORDER BY LINE
    """

    cursor = conn.cursor()
    cursor.execute(query, {'procedure_name': procedure_name.upper()})
    source_code = "".join(row[0] for row in cursor.fetchall())
    cursor.close()

    return source_code


def compare_procedures(conn1, conn2, proc1, proc2):
    """
    Compara duas procedures de bancos diferentes e exibe as diferenças.
    """
    source1 = get_procedure_source(conn1, proc1).splitlines()
    source2 = get_procedure_source(conn2, proc2).splitlines()

    diff = difflib.unified_diff(source1, source2, lineterm='',
                                fromfile=f"Banco 1: {proc1}", tofile=f"Banco 2: {proc2}")

    print("\n".join(diff) if source1 and source2 else "Uma ou ambas as procedures não foram encontradas.")


if __name__ == "__main__":
    dsn1 = cx_Oracle.makedsn("host1", "port1", service_name="service1")
    conn1 = cx_Oracle.connect(user="usuario1", password="senha1", dsn=dsn1)

    dsn2 = cx_Oracle.makedsn("host2", "port2", service_name="service2")
    conn2 = cx_Oracle.connect(user="usuario2", password="senha2", dsn=dsn2)

    procedure1 = input("Digite o nome da procedure no primeiro banco: ")
    procedure2 = input("Digite o nome da procedure no segundo banco: ")

    compare_procedures(conn1, conn2, procedure1, procedure2)

    conn1.close()
    conn2.close()