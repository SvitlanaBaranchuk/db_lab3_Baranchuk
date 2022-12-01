SELECT * FROM Video_Rating;
CREATE TABLE Video_Rating_Copy AS SELECT * FROM Video_Rating; 
DELETE FROM Video_Rating_Copy;
SELECT * FROM Video_Rating_Copy;


DO $$
 DECLARE
	 video_id Video_Rating_Copy.video_id%TYPE;
	 likes Video_Rating_Copy.likes%TYPE;
	 dislikes Video_Rating_Copy.dislikes%TYPE;
	 v_views Video_Rating_Copy.v_views%TYPE;
	 coments Video_Rating_Copy.coments%TYPE;

 BEGIN
     video_id := 1;
	 likes := 100;
	 dislikes := 10;
	 v_views := 500;
	 coments := 50;
	 
     FOR counter IN 1..20
         LOOP
            INSERT INTO video_rating_copy (video_id, act_date, likes, dislikes, v_views, coments)
             VALUES (counter || video_id, current_date - counter + 1, counter + likes, counter + dislikes, counter + v_views, counter + coments);
         END LOOP;
 END;
 $$