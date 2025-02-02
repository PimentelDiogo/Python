DECLARE
    v_proc1 CLOB;
    v_proc2 CLOB;
    v_diff  PLS_INTEGER;
BEGIN
    -- Obtém o código-fonte das duas procedures
    SELECT LISTAGG(TEXT, '') WITHIN GROUP (ORDER BY LINE) INTO v_proc1
    FROM ALL_SOURCE WHERE NAME = 'PROCEDURE_1' AND TYPE = 'PROCEDURE';

    SELECT LISTAGG(TEXT, '') WITHIN GROUP (ORDER BY LINE) INTO v_proc2
    FROM ALL_SOURCE WHERE NAME = 'PROCEDURE_2' AND TYPE = 'PROCEDURE';

    -- Compara os conteúdos das duas procedures
    v_diff := DBMS_LOB.COMPARE(v_proc1, v_proc2);

    IF v_diff = 0 THEN
        DBMS_OUTPUT.PUT_LINE('As procedures são idênticas.');
    ELSE
        DBMS_OUTPUT.PUT_LINE('As procedures são diferentes.');
    END IF;
END;
/

/*Extrai o código-fonte de duas procedures (PROCEDURE_1 e PROCEDURE_2).
Usa LISTAGG para concatenar as linhas de código.
Compara os códigos com DBMS_LOB.COMPARE.*/