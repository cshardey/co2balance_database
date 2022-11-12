--- TRIGGER  FUNCTION TO CHECK IF NAME EXISTS IN THE TABLE THEN UPDATE THE RECORD ELSE INSERT THE RECORD ---
CREATE OR REPLACE FUNCTION check_name_exists()
RETURNS TRIGGER AS $$
DECLARE
    v_count integer;
BEGIN
    SELECT COUNT(*) INTO v_count FROM test WHERE name = NEW.name;
    IF v_count > 0 THEN
        UPDATE test SET name = NEW.name WHERE name = NEW.name;
    ELSE
        INSERT INTO test (name) VALUES (NEW.name);
    END IF;
    RETURN NULL;
END;
