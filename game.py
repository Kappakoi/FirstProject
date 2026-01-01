diff --git a/game.py b/game.py
index b456aa0..24235ff 100644
--- a/game.py
+++ b/game.py
@@ -1,11 +1,15 @@
 from __future__ import annotations
 
-from dataclasses import dataclass
+from dataclasses import dataclass, field
 from random import Random
 from typing import Iterable, List
 
 RNG = Random()
 
+# Tunable knobs for short sessions.
+STAGE_ENEMIES_BASE = 3
+STAGE_ENEMIES_STEP = 2
+
 
 @dataclass(frozen=True)
 class EnemyType:
@@ -66,11 +70,11 @@ class Player:
 class GameState:
     stage: int = 1
     enemies_defeated: int = 0
-    player: Player = Player()
+    player: Player = field(default_factory=Player)
 
     def enemies_per_stage(self) -> int:
         # Keep stages short and punchy.
-        return 3 + self.stage // 2
+        return STAGE_ENEMIES_BASE + self.stage // STAGE_ENEMIES_STEP
 
     def available_enemies(self) -> Iterable[EnemyType]:
         return [enemy for enemy in ENEMY_ROSTER if enemy.unlock_stage <= self.stage]
@@ -95,7 +99,7 @@ def player_damage(level: int, stage: int) -> int:
     if level < 1 or stage < 1:
         raise ValueError("level and stage must be >= 1")
     # Player damage scales to keep combat brisk per stage.
-    return 6 + level * 2 + stage
+    return 6 + level * 2 + stage * 2
 
 
 def enemy_damage(enemy: EnemyStats) -> int:
