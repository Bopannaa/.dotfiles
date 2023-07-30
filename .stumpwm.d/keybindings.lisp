(defvar *move-to-keybinds* (list "!" "@" "#" "$" "%" "^" "&" "*" "("))
(dotimes (y (length *ce/workspaces*))
  (let ((workspace (write-to-string (+ y 1))))
    (define-key *top-map* (kbd (concat "s-" workspace)) (concat "gselect " workspace))
    (define-key *top-map* (kbd (concat "s-" (nth y *move-to-keybinds*))) (concat "gmove-and-follow " workspace))))


(define-key *root-map* (kbd "Q") "quit")
(define-key *root-map* (kbd "R") "restart-hard")

(define-key *root-map* (kbd "q") "delete")
(define-key *root-map* (kbd "r") "remove")

(define-key *root-map* (kbd "h") "move-focus left")
(define-key *root-map* (kbd "j") "move-focus down")
(define-key *root-map* (kbd "k") "move-focus up")
(define-key *root-map* (kbd "l") "move-focus right")
(define-key *root-map* (kbd "H") "move-window left")
(define-key *root-map* (kbd "J") "move-window down")
(define-key *root-map* (kbd "K") "move-window up")
(define-key *root-map* (kbd "L") "move-window right")

(setf *resize-increment* 50)
(define-key *top-map* (kbd "M-l") "resize-direction Right")
(define-key *top-map* (kbd "M-h") "resize-direction Left")
(define-key *top-map* (kbd "M-k") "resize-direction Up")
(define-key *top-map* (kbd "M-j") "resize-direction Down")

(define-key *top-map* (kbd "s-RET") "exec alacritty")
(define-key *top-map* (kbd "s-q") "delete")
(define-key *top-map* (kbd "s-d") "exec rofi -show drun")
(define-key *top-map* (kbd "s-f") "exec rofi -show filebrowser")
(define-key *top-map* (kbd "s-w") "exec rofi -show windowcd")
