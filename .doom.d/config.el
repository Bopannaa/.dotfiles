;; Load up doom-palenight for the System Crafters look
(load-theme 'doom-palenight t)

;; NOTE: These settings might not be ideal for your machine, tweak them as needed!
(set-face-attribute 'default nil :font "JetBrains Mono" :weight 'light :height 110)
(set-face-attribute 'fixed-pitch nil :font "JetBrains Mono" :weight 'light :height 120)
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


;; add to $DOOMDIR/config.el
(add-hook! 'rainbow-mode-hook
  (hl-line-mode (if rainbow-mode -1 +1)))

(setq lsp-julia-package-dir nil)
(use-package lsp-julia
  :config
  (setq lsp-julia-default-environment "~/.julia/environments/v1.9"))
