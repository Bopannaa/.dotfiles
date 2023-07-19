;; (require 'exwm)
;; (require 'exwm-config)
;; (exwm-config-default)
;; (require 'exwm-randr)
;; (setq exwm-randr-workspace-output-plist '(0 "LVDS-1"))
;; (add-hook 'exwm-randr-screen-change-hook
;;           (lambda ()
;;           (start-process-shell-command
;;           "xrandr" nil "--output LVDS-1 --mode 1366x768 --pos 0x0 --rotate normal")))
;; (exwm-randr-enable)
;; (require 'exwm-systemtray)
;; (exwm-systemtray-enable)


;;(setq doom-font (font-spec :family "Fira Mono" :size 18))

;; Load up doom-palenight for the System Crafters look
(load-theme 'doom-palenight t)

;; NOTE: These settings might not be ideal for your machine, tweak them as needed!
(set-face-attribute 'default nil :font "JetBrains Mono" :weight 'light :height 140)
(set-face-attribute 'fixed-pitch nil :font "JetBrains Mono" :weight 'light :height 150)
(set-face-attribute 'variable-pitch nil :font "Iosevka Aile" :weight 'light :height 1.3)


(map! "C-," #'+workspace:switch-next)

(use-package shr-tag-pre-highlight
  :ensure t
  :after shr
  :config
  (add-to-list 'shr-external-rendering-functions
               '(pre . shr-tag-pre-highlight))
  (when (version< emacs-version "26")
    (with-eval-after-load 'eww
      (advice-add 'eww-display-html :around
                  'eww-display-html--override-shr-external-rendering-functions))))
