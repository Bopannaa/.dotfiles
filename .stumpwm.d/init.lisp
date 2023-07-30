(in-package :stumpwm)

(run-shell-command "nitrogen --restore")
(run-shell-command "picom")

;; (setf *message-window-gravity* :center
;;       *input-window-gravity* :center
;;       *window-border-style* :thin
;;       *message-window-padding* 10
;;       *maxsize-border-width* 2
;;       *normal-border-width* 2
;;       *transient-border-width* 2
;;       stumpwm::*float-window-border* 4
;;       stumpwm::*float-window-title-height* 20
;;       *mouse-focus-policy* :click)

(defun show-kernel ()
  (let ((ip (run-shell-command "uname -r" t)))
    (substitute #\Space #\Newline ip)))

(defun show-hostname ()
  (let ((host-name (run-shell-command "cat /etc/hostname" t)))
    (substitute #\Space #\Newline host-name)))

(defun show-package-count ()
  (let ((host-name (run-shell-command "pacman -Q | wc -l" t)))
    (substitute #\Space #\Newline host-name)))

(defvar color1 "#ff92d0")
(defvar color2 "#282a36")

(setf
 stumpwm:*mode-line-background-color* color2
 stumpwm:*mode-line-foreground-color* color1
 stumpwm:*mode-line-border-color* "#333333"
 stumpwm:*screen-mode-line-format* (list "%g | %v ^>^7 | " '(:eval (show-hostname)) "| " '(:eval (show-kernel)) "| " '(:eval (show-package-count)) "packages | %d ")
 stumpwm:*mode-line-border-width* 1
 stumpwm:*mode-line-pad-x* 6
 stumpwm:*mode-line-pad-y* 1
 stumpwm:*mode-line-timeout* 5
 stumpwm:*mouse-focus-policy* :click
 stumpwm:*group-format* "%n·%t"
 stumpwm:*time-modeline-string* "%a, %b %d, %Y %l:%M%p"
 stumpwm:*window-format* "^b^(:fg \"#9aedfe\")<%25t>"
 stumpwm:*window-border-style* :tight
 stumpwm:*normal-border-width* 1
 )
(stumpwm:set-focus-color "#7799CC")
;; (stumpwm:grename "Alpha")
;; (stumpwm:gnewbg "Beta")
;; (stumpwm:gnewbg "Tau")
;; (stumpwm:gnewbg "Pi")
;; (stumpwm:gnewbg "Zeta")
;; (stumpwm:gnewbg "Teta")
;; (stumpwm:gnewbg "Phi")
;; (stumpwm:gnewbg "Rho")

(set-prefix-key (kbd "C-z"))

(defvar *ce/workspaces* (list "WWW" "Code" "Term"))
(stumpwm:grename (nth 0 *ce/workspaces*))
(dolist (workspace (cdr *ce/workspaces*))
  (stumpwm:gnewbg workspace))
(set-font "-xos4-terminus-medium-r-normal--14-140-72-72-c-80-iso8859-14")
(stumpwm:toggle-mode-line (stumpwm:current-screen) (stumpwm:current-head))

(load "~/.stumpwm.d/keybindings.lisp")
