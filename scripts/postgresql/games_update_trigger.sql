CREATE OR REPLACE FUNCTION games_update_notify() RETURNS trigger as $$
BEGIN
	PERFORM pg_notify('games_update'::text, row_to_json(NEW)::text);
	RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS games_update_trigger ON game;

CREATE TRIGGER games_update_trigger AFTER INSERT OR UPDATE ON game
	FOR EACH ROW
	EXECUTE PROCEDURE games_update_notify();