-- Standard awesome library
local awful = require("awful")

local _M = {}

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

function _M.get ()
  -- Table of layouts to cover with awful.layout.inc, order matters.
  local layouts = {
    awful.layout.suit.tile.left,        -- 3:
    awful.layout.suit.floating,           -- 1:
    awful.layout.suit.max,                -- 10:
  }

  return layouts
end

-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --

return setmetatable({}, { __call = function(_, ...) return _M.get(...) end })
