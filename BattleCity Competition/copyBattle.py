
#########################<BEGINNING OF PROGRAM>##################
import sys
import codecs
import random
from time import clock
from pickle import load
stng = 'abandon-abandoned-ability-able-about-above-abroad-absence-absent-absolute-absolutely-absorb-abuse-academic-accent-accept-acceptable-access-accident-accidental-accidentally-accommodation-accompany-according-account-accurate-accurately-accuse-achieve-achievement-acid-acknowledge-a-acquire-across-act-action-active-actively-activity-actor-actress-actual-actually-ad-adapt-add-addition-additional-add-address-add-adequate-adequately-adjust-admiration-admire-admit-adopt-adult-advance-advanced-advantage-adventure-advert-advertise-advertisement-advertising-advice-advise-affair-affect-affection-afford-afraid-after-afternoon-afterwards-again-against-age-aged-agency-agent-aggressive-ago-agree-agreement-ahead-aid-aim-air-aircraft-airport-alarm-alarmed-alarming-alcohol-alcoholic-alive-all-allied-allow-all-ally-almost-alone-along-alongside-aloud-alphabet-alphabetical-alphabetically-already-also-alter-alternative-alternatively-although-altogether-always-am-amaze-amazed-amazing-ambition-ambulance-among-amount-amuse-amused-amusing-analyse-analysis-ancient-and-anger-angle-angrily-angry-animal-ankle-anniversary-announce-annoy-annoyed-annoying-annual-annually-another-answer-anti-anticipate-anxiety-anxious-anxiously-any-anybody-anyone-anything-anyway-anywhere-apart-apartment-apologize-apparent-apparently-appeal-appear-appearance-apple-application-apply-appoint-appointment-appreciate-approach-appropriate-approval-approve-approving-approximate-approximately-april-area-argue-argument-arise-arm-armed-arms-army-around-arrange-arrangement-arrest-arrival-arrive-arrow-art-article-artificial-artificially-artist-artistic-artistically-as-ashamed-aside-ask-asleep-aspect-assist-assistance-assistant-associate-associated-association-assume-assure-at-atmosphere-atom-attach-attached-attack-attempt-attempted-attend-attention-attitude-attorney-attract-attraction-attractive-audience-august-aunt-author-authority-automatic-automatically-autumn-available-average-avoid-awake-award-aware-away-awful-awfully-awkward-awkwardly-baby-back-background-back-backward-backwards-bacteria-bad-badly-badtempered-bag-baggage-bake-balance-ball-ban-band-bandage-bank-bar-bargain-barrier-base-based-base-basic-basically-basis-bath-bathroom-battery-battle-bay-be-beach-beak-bear-beard-beat-beautiful-beautifully-beauty-because-become-bed-bedroom-beef-beer-before-begin-beginning-behalf-behave-behaviour-behind-be-belief-believe-bell-belong-below-belt-bend-beneath-benefit-bent-beside-best-bet-better-betting-between-beyond-bicycle-bid-big-bike-bill-billion-bin-biology-bird-birth-birthday-biscuit-bit-bite-bitter-bitterly-black-blade-blame-blank-blind-block-blonde-blood-blow-blue-board-boat-body-boil-bomb-bone-book-boot-border-bore-bored-boring-born-borrow-boss-both-bother-bottle-bottom-bound-bowl-box-boy-boyfriend-brain-branch-brand-brave-bread-break-breakfast-break-breast-breath-breathe-breathing-breed-brick-bridge-brief-briefly-bright-brightly-brilliant-bring-broad-broadcast-broadly-broken-brother-brown-brush-bubble-budget-build-building-build-bullet-bunch-burn-burnt-burst-bury-bus-bush-business-businessman-busy-but-butter-button-buy-buyer-by-bye-cabinet-cable-cake-calculate-calculation-call-called-call-calm-calmly-camera-camp-campaign-camping-can-cancel-cancer-candidate-candy-cannot-cap-capable-capacity-capital-captain-capture-car-card-cardboard-care-career-care-careful-carefully-careless-carelessly-carpet-carrot-carry-case-cash-cast-castle-cat-catch-category-cause-cd-cease-ceiling-celebrate-celebration-cell-cent-centimetre-central-centre-century-ceremony-certain-certainly-certificate-chain-chair-chairman-chairwoman-challenge-chamber-chance-change-channel-chapter-character-characteristic-charge-charity-chart-chase-chat-cheap-cheaply-cheat-check-check-cheek-cheerful-cheerfully-cheese-chemical-chemist-chemistry-cheque-chest-chew-chicken-chief-child-chin-chip-chocolate-choice-choose-chop-church-cigarette-cinema-circle-circumstance-citizen-city-civil-claim-clap-class-classic-classroom-clean-clear-clearly-clear-clerk-clever-click-client-climate-climb-climbing-clock-close-closed-closely-closet-cloth-clothes-clothing-cloud-club-coach-coal-coast-coat-code-coffee-coin-cold-coldly-collapse-colleague-collect-collection-college-colour-coloured-column-combination-combine-come-comedy-come-comfort-comfortable-comfortably-command-comment-commercial-commission-commit-commitment-committee-common-commonly-communicate-communication-community-company-compare-comparison-compete-competition-competitive-complain-complaint-complete-completely-complex-complicate-complicated-computer-concentrate-concentration-concept-concern-concerned-concerning-concert-conclude-conclusion-concrete-condition-conduct-conference-confidence-confident-confidently-confine-confined-confirm-conflict-confront-confuse-confused-confusing-confusion-congratulate-congratulation-congress-connect-connected-connection-conscious-consequence-conservative-consider-considerable-considerably-consideration-consist-constant-constantly-construct-construction-consult-consumer-contact-contain-container-contemporary-content-contest-context-continent-continue-continuous-continuously-contract-contrast-contrasting-contribute-contribution-control-controlled-convenient-convention-conventional-conversation-convert-convince-cook-cooker-cookie-cooking-cool-cope-copy-core-corner-correct-correctly-cost-cottage-cotton-cough-coughing-could-council-count-counter-count-country-countryside-county-couple-courage-course-court-cousin-cover-covered-covering-cover-cow-crack-cracked-craft-crash-crazy-cream-create-creature-credit-crime-criminal-crisis-crisp-criterion-critical-criticism-criticize-crop-cross-crowd-crowded-crown-crucial-cruel-crush-cry-cultural-culture-cup-cupboard-curb-cure-curious-curiously-curl-curly-current-currently-curtain-curve-curved-custom-customer-customs-cut-cycle-cycling-dad-daily-damage-damp-dance-dancer-dancing-danger-dangerous-dare-dark-data-date-daughter-day-dead-deaf-deal-dear-death-debate-debt-decade-decay-december-decide-decision-declare-decline-decorate-decoration-decorative-decrease-deep-deeply-defeat-defence-defend-define-definite-definitely-definition-degree-delay-deliberate-deliberately-delicate-delight-delighted-deliver-delivery-demand-demonstrate-dentist-deny-department-departure-depend-deposit-depress-depressed-depressing-depth-derive-describe-description-desert-deserted-deserve-design-desire-desk-desperate-desperately-despite-destroy-destruction-detail-detailed-determination-determine-determined-develop-development-device-devote-devoted-devote-diagram-diamond-diary-dictionary-die-diet-difference-different-differently-difficult-difficulty-dig-digital-dinner-direct-direction-directly-director-dirt-dirty-disabled-disadvantage-disagree-disagreement-disagree-disappear-disappoint-disappointed-disappointing-disappointment-disapproval-disapprove-disapproving-disaster-disc-discipline-discount-discover-discovery-discuss-discussion-disease-disgust-disgusted-disgusting-dish-dishonest-dishonestly-disk-dislike-dismiss-display-dissolve-distance-distinguish-distribute-distribution-district-disturb-disturbing-divide-division-divorce-divorced-do-doctor-document-dog-dollar-domestic-dominate-door-dot-double-doubt-do-down-downstairs-downward-downwards-dozen-draft-drag-drama-dramatic-dramatically-draw-drawer-drawing-dream-dress-dressed-dress-drink-drive-driver-driving-drop-drug-drugstore-drum-drunk-dry-due-dull-dump-during-dust-duty-dvd-dying-each-ear-early-earn-earth-ease-easily-east-eastern-easy-eat-economic-economy-edge-edition-editor-educate-educated-education-effect-effective-effectively-efficient-efficiently-effort-eg-egg-eight-eighteen-eighteenth-eighth-eightieth-eighty-either-elbow-elderly-elect-election-electric-electrical-electricity-electronic-elegant-element-elevator-eleven-eleventh-else-elsewhere-email-embarrass-embarrassed-embarrassing-embarrassment-emerge-emergency-emotion-emotional-emotionally-emphasis-emphasize-empire-employ-employee-employer-employment-empty-enable-encounter-encourage-encouragement-end-ending-end-enemy-energy-engage-engaged-engine-engineer-engineering-enjoy-enjoyable-enjoyment-enormous-enough-enquiry-ensure-enter-entertain-entertainer-entertaining-entertainment-enthusiasm-enthusiastic-enthusiastically-entire-entirely-entitle-entrance-entry-envelope-environment-environmental-equal-equally-equipment-equivalent-error-escape-especially-essay-essential-essentially-establish-estate-estimate-etc-euro-even-evening-event-eventually-ever-every-everybody-everyone-everything-everywhere-evidence-evil-ex-exact-exactly-exaggerate-exaggerated-exam-examination-examine-example-excellent-except-exception-exchange-excite-excited-excitement-exciting-exclude-excluding-excuse-executive-exercise-exhibit-exhibition-exist-existence-exit-expand-expect-expectation-expected-expense-expensive-experience-experienced-experiment-expert-explain-explanation-explode-explore-explosion-export-expose-express-expression-extend-extension-extensive-extent-extra-extraordinary-extreme-extremely-eye-face-facility-fact-factor-factory-fail-failure-faint-faintly-fair-fairly-faith-faithful-faithfully-fall-false-fame-familiar-family-famous-fan-fancy-far-farm-farmer-farming-farther-farthest-fashion-fashionable-fast-fasten-fat-father-faucet-fault-favour-favourite-fear-feather-feature-february-federal-fee-feed-feel-feeling-fellow-female-fence-festival-fetch-fever-few-field-fifteen-fifteenth-fifth-fiftieth-fifty-fight-fighting-figure-file-fill-film-final-finally-finance-financial-find-fine-finely-finger-finish-finished-finish-fire-firm-firmly-first-fish-fishing-fit-five-fix-fixed-flag-flame-flash-flat-flavour-flesh-flight-float-flood-flooded-flooding-floor-flour-flow-flower-flu-fly-flying-focus-fold-folding-follow-following-follow-food-foot-football-for-force-forecast-foreign-forest-forever-forget-forgive-fork-form-formal-formally-former-formerly-formula-fortieth-fortune-forty-forward-found-foundation-four-fourteen-fourteenth-fourth-frame-free-freedom-freely-freeze-frequent-frequently-fresh-freshly-friday-fridge-friend-friendly-friendship-frighten-frightened-frightening-from-front-frozen-fruit-fry-fuel-full-fully-fun-function-fund-fundamental-funeral-funny-fur-furniture-further-future-gain-gallon-gamble-gambling-game-gap-garage-garbage-garden-gas-gasoline-gate-gather-gear-general-generally-generate-generation-generous-generously-gentle-gentleman-gently-genuine-genuinely-geography-get-giant-gift-girl-girlfriend-give-glad-glass-global-glove-glue-go-goal-go-god-go-gold-good-goodbye-goods-go-govern-government-governor-go-grab-grade-gradual-gradually-grain-gram-grammar-grand-grandchild-granddaughter-grandfather-grandmother-grandparent-grandson-grant-grass-grateful-grave-gravely-great-greatly-green-grey-grocery-ground-group-grow-growth-grow-guarantee-guard-guess-guest-guide-guilty-gun-guy-habit-hair-hairdresser-half-hall-hammer-hand-handle-hand-hang-happen-happily-happiness-happy-hard-hardly-harm-harmful-harmless-hat-hate-hatred-have-he-head-headache-heal-health-healthy-hear-hearing-hear-heart-heat-heating-heat-heaven-heavily-heavy-heel-height-hell-hello-help-helpful-help-hence-her-here-hero-hers-herself-hesitate-hi-hide-high-highlight-highly-highway-hill-him-himself-hip-hire-his-historical-history-hit-hobby-hold-hole-holiday-hollow-holy-home-homework-honest-honestly-honour-hook-hope-horizontal-horn-horror-horse-hospital-host-hot-hotel-hour-house-household-housing-how-however-huge-human-humorous-humour-hundred-hundredth-hungry-hunt-hunting-hurry-hurt-husband-i-ice-idea-ideal-identify-identity-ie-if-ignore-ill-illegal-illegally-illness-illustrate-image-imaginary-imagination-imagine-immediate-immediately-immoral-impact-impatient-implication-imply-import-importance-important-importantly-impose-impossible-impress-impressed-impression-impressive-improve-improvement-in-inability-inch-incident-include-including-income-increase-increasingly-indeed-independence-independent-independently-index-indicate-indication-indirect-indirectly-individual-indoor-indoors-industrial-industry-inevitable-inevitably-infect-infected-infection-infectious-influence-inform-informal-information-ingredient-initial-initially-initiative-injure-injured-injury-ink-inner-innocent-insect-insert-inside-insist-install-instance-instead-institute-institution-instruction-instrument-insult-insulting-insurance-intelligence-intelligent-intend-intended-intention-interest-interested-interesting-interior-internal-international-internet-interpret-interpretation-interrupt-interruption-interval-interview-into-introduce-introduction-invent-invention-invest-investigate-investigation-investment-invitation-invite-involve-involved-involvement-iron-irritate-irritated-irritating-island-issue-it-item-its-itself-jacket-jam-january-jealous-jeans-jelly-jewellery-job-join-joint-jointly-joke-journalist-journey-joy-judge-judgement-juice-july-jump-june-junior-just-justice-justified-justify-keen-keep-key-keyboard-kick-kid-kill-killing-kilogram-kilometre-kind-kindly-kindness-king-kiss-kitchen-knee-knife-knit-knitted-knitting-knock-knot-know-knowledge-lab-label-laboratory-labour-lack-lacking-lady-lake-lamp-land-landscape-lane-language-large-largely-last-late-later-latest-latter-laugh-launch-law-lawyer-lay-layer-lazy-lead-leader-leading-leaf-league-lean-learn-least-leather-leave-lecture-left-leg-legal-legally-lemon-lend-length-less-lesson-let-letter-level-library-licence-license-lid-lie-life-lift-light-lightly-like-likely-limit-limited-limit-line-link-lip-liquid-list-listen-literature-litre-little-live-lively-live-living-load-loan-local-locally-locate-located-location-lock-logic-logical-lonely-long-look-loose-loosely-lord-lorry-lose-loss-lost-lot-loud-loudly-love-lovely-lover-low-loyal-luck-lucky-luggage-lump-lunch-lung-machine-machinery-mad-magazine-magic-mail-main-mainly-maintain-major-majority-make-makeup-make-male-mall-man-manage-management-manager-manner-manufacture-manufacturer-manufacturing-many-map-march-march-mark-market-marketing-marriage-married-marry-mass-massive-master-match-matching-match-mate-material-mathematics-matter-maximum-may-may-maybe-mayor-me-meal-mean-meaning-means-meanwhile-measure-measurement-meat-media-medical-medicine-medium-meet-meeting-meet-melt-member-membership-memory-mental-mentally-mention-menu-mere-merely-mess-message-metal-method-metre-mid-midday-middle-midnight-might-mild-mile-military-milk-milligram-millimetre-million-millionth-mind-mine-mineral-minimum-minister-ministry-minor-minority-minute-mirror-miss-missing-miss-mistake-mistaken-mix-mixed-mixture-mix-mobile-model-modern-mom-moment-monday-money-monitor-month-mood-moon-moral-morally-more-moreover-morning-most-mostly-mother-motion-motor-motorbike-motorcycle-mount-mountain-mouse-mouth-move-movement-move-movie-moving-mr-mrs-ms-much-mud-multiply-mum-murder-muscle-museum-music-musical-musician-must-my-myself-mysterious-mystery-nail-naked-name-narrow-nation-national-natural-naturally-nature-navy-near-nearby-nearly-neat-neatly-necessarily-necessary-neck-need-needle-negative-neighbour-neighbourhood-neither-nephew-nerve-nervous-nervously-nest-net-network-never-nevertheless-new-newly-news-newspaper-next-nice-nicely-niece-night-nine-nineteen-nineteenth-ninetieth-ninety-ninth-no-nobody-noise-noisily-noisy-non-none-nonsense-no-nor-normal-normally-north-northern-nose-not-note-nothing-notice-noticeable-novel-november-now-nowhere-nuclear-number-nurse-nut-obey-object-objective-observation-observe-obtain-obvious-obviously-occasion-occasionally-occupied-occupy-occur-ocean-"oclock", october-odd-oddly-of-off-offence-offend-offense-offensive-offer-office-officer-official-officially-often-oh-oil-ok-old-oldfashioned-on-once-one-onion-online-only-onto-open-opening-openly-open-operate-operation-opinion-opponent-opportunity-oppose-opposed-opposing-opposite-opposition-option-or-orange-order-ordinary-organ-organization-organize-organized-origin-original-originally-other-otherwise-ought-our-ours-ourselves-out-outdoor-outdoors-outer-outline-output-outside-outstanding-oven-over-overall-overcome-owe-own-owner-own-pace-pack-package-packaging-packet-pack-page-pain-painful-paint-painter-painting-pair-palace-pale-pan-panel-pants-paper-parallel-parent-park-parliament-part-particular-particularly-partly-partner-partnership-party-pass-passage-pass-passenger-passing-pass-passport-pass-past-path-patience-patient-pattern-pause-pay-payment-pay-peace-peaceful-peak-pen-pencil-penny-pension-people-pepper-per-perfect-perfectly-perform-performance-performer-perhaps-period-permanent-permanently-permission-permit-person-personal-personality-personally-persuade-pet-petrol-phase-philosophy-phone-photo-photocopy-photograph-photographer-photography-phrase-physical-physically-physics-piano-pick-picture-piece-pig-pile-pill-pilot-pin-pink-pint-pipe-pitch-pity-place-plain-plan-plane-planet-planning-plant-plastic-plate-platform-play-player-play-pleasant-pleasantly-please-pleased-pleasing-pleasure-plenty-plot-plug-plus-pm-pocket-poem-poetry-point-pointed-point-poison-poisonous-pole-police-policy-polish-polite-politely-political-politically-politician-politics-pollution-pool-poor-pop-popular-population-port-pose-position-positive-possess-possession-possibility-possible-possibly-post-pot-potato-potential-potentially-pound-pour-powder-power-powerful-practical-practically-practice-practise-praise-pray-prayer-precise-precisely-predict-prefer-preference-pregnant-premises-preparation-prepare-prepared-presence-present-presentation-preserve-president-press-pressure-presumably-pretend-pretty-prevent-previous-previously-price-pride-priest-primarily-primary-prime-prince-princess-principle-print-printer-printing-print-prior-priority-prison-prisoner-private-privately-prize-probable-probably-problem-procedure-proceed-process-produce-producer-product-production-profession-professional-professor-profit-program-programme-progress-project-promise-promote-promotion-prompt-promptly-pronounce-pronunciation-proof-proper-properly-property-proportion-proposal-propose-prospect-protect-protection-protest-proud-proudly-prove-provide-provided-providing-pub-public-publication-publicity-publicly-publish-publishing-pull-punch-punish-punishment-pupil-purchase-pure-purely-purple-purpose-pursue-push-put-qualification-qualified-qualify-quality-quantity-quarter-queen-question-quick-quickly-quiet-quietly-quit-quite-quote-race-racing-radio-rail-railroad-railway-rain-raise-range-rank-rapid-rapidly-rare-rarely-rate-rather-raw-re-reach-react-reaction-read-reader-reading-read-ready-real-realistic-reality-realize-really-rear-reason-reasonable-reasonably-recall-receipt-receive-recent-recently-reception-reckon-recognition-recognize-recommend-record-recording-recover-red-reduce-reduction-refer-reference-refer-reflect-reform-refrigerator-refusal-refuse-regard-regarding-region-regional-register-regret-regular-regularly-regulation-reject-relate-related-relate-relation-relationship-relative-relatively-relax-relaxed-relaxing-release-relevant-relief-religion-religious-rely-remain-remaining-remains-remark-remarkable-remarkably-remember-remind-remote-removal-remove-rent-rented-repair-repeat-repeated-repeatedly-replace-reply-report-represent-representative-reproduce-reputation-request-require-requirement-rescue-research-reservation-reserve-resident-resist-resistance-resolve-resort-resource-respect-respond-response-responsibility-responsible-rest-restaurant-restore-restrict-restricted-restriction-result-retain-retire-retired-retirement-return-reveal-reverse-review-revise-revision-revolution-reward-rhythm-rice-rich-rid-ride-rider-ridiculous-riding-right-rightly-ring-rise-risk-rival-river-road-rob-rock-role-roll-romantic-roof-room-root-rope-rough-roughly-round-rounded-route-routine-row-royal-rub-rubber-rubbish-rude-rudely-ruin-ruined-rule-ruler-rumour-run-runner-running-run-rural-rush-sack-sad-sadly-sadness-safe-safely-safety-sail-sailing-sailor-salad-salary-sale-salt-salty-same-sample-sand-satisfaction-satisfied-satisfy-satisfying-saturday-sauce-save-saving-say-scale-scare-scared-scare-scene-schedule-scheme-school-science-scientific-scientist-scissors-score-scratch-scream-screen-screw-sea-seal-search-season-seat-second-secondary-secret-secretary-secretly-section-sector-secure-security-see-seed-seek-seem-see-select-selection-self-self-sell-senate-senator-send-senior-sense-sensible-sensitive-sentence-separate-separated-separately-separation-september-series-serious-seriously-servant-serve-service-session-set-settle-set-seven-seventeen-seventh-seventieth-seventy-several-severe-severely-sew-sewing-sex-sexual-sexually-shade-shadow-shake-shall-shallow-shame-shape-shaped-share-sharp-sharply-shave-she-sheep-sheet-shelf-shell-shelter-shift-shine-shiny-ship-shirt-shock-shocked-shocking-shoe-shoot-shooting-shop-shopping-short-shortly-shot-should-shoulder-shout-show-shower-show-shut-shy-sick-side-sideways-sight-sign-signal-signature-significant-significantly-silence-silent-silk-silly-silver-similar-similarly-simple-simply-since-sincere-sincerely-sing-singer-singing-single-sink-sir-sister-sit-site-situation-six-sixteen-sixth-sixtieth-sixty-size-skilful-skilfully-skill-skilled-skin-skirt-sky-sleep-sleeve-slice-slide-slight-slightly-slip-slope-slow-slowly-small-smart-smash-smell-smile-smoke-smoking-smooth-smoothly-snake-snow-so-soap-social-socially-society-sock-soft-softly-software-soil-soldier-solid-solution-solve-some-somebody-somehow-someone-something-sometimes-somewhat-somewhere-son-song-soon-sore-sorry-sort-soul-sound-soup-sour-source-south-southern-space-spare-speak-speaker-speak-special-specialist-specially-specific-specifically-speech-speed-spell-spelling-spend-spice-spicy-spider-spin-spirit-spiritual-spite-split-spoil-spoken-spoon-sport-spot-spray-spread-spring-square-squeeze-stable-staff-stage-stair-stamp-stand-standard-stand-star-stare-start-state-statement-station-statue-status-stay-steadily-steady-steal-steam-steel-steep-steeply-steer-step-stick-sticky-stiff-stiffly-still-sting-stir-stock-stomach-stone-stop-store-storm-story-stove-straight-strain-strange-strangely-stranger-strategy-stream-street-strength-stress-stressed-stretch-strict-strictly-strike-striking-string-strip-stripe-striped-stroke-strong-strongly-structure-struggle-student-studio-study-stuff-stupid-style-subject-substance-substantial-substantially-substitute-succeed-success-successful-successfully-such-suck-sudden-suddenly-suffer-suffering-sufficient-sufficiently-sugar-suggest-suggestion-suit-suitable-suitcase-suited-sum-summary-summer-sum-sun-sunday-superior-supermarket-supply-support-supporter-suppose-sure-surely-surface-surname-surprise-surprised-surprising-surprisingly-surround-surrounding-surroundings-survey-survive-suspect-suspicion-suspicious-swallow-swear-swearing-sweat-sweater-sweep-sweet-swell-swelling-swim-swimming-swing-switch-swollen-symbol-sympathetic-sympathy-system-table-tablet-tackle-tail-take-talk-tall-tank-tap-tape-target-task-taste-tax-taxi-tea-teach-teacher-teaching-team-tear-technical-technique-technology-telephone-television-tell-temperature-temporarily-temporary-ten-tend-tendency-tension-tent-tenth-term-terrible-terribly-test-text-than-thank-thanks-thank-that-the-theatre-their-theirs-them-theme-themselves-then-theory-there-therefore-they-thick-thickly-thickness-thief-thin-thing-think-thinking-think-third-thirsty-thirteen-thirteenth-thirtieth-thirty-this-thorough-thoroughly-though-thought-thousand-thousandth-thread-threat-threaten-threatening-three-throat-through-throughout-throw-thumb-thursday-thus-ticket-tidy-tie-tight-tightly-till-time-timetable-tin-tiny-tip-tire-tired-tire-tiring-title-to-today-toe-together-toilet-tomato-tomorrow-ton-tone-tongue-tonight-tonne-too-tool-tooth-top-topic-total-totally-touch-tough-tour-tourist-towards-towel-tower-town-toy-trace-track-trade-trading-tradition-traditional-traditionally-traffic-train-training-transfer-transform-translate-translation-transparent-transport-transportation-trap-travel-traveller-treat-treatment-tree-trend-trial-triangle-trick-trip-tropical-trouble-trousers-truck-true-truly-trust-truth-try-tube-tuesday-tune-tunnel-turn-tv-twelfth-twelve-twentieth-twenty-twice-twin-twist-twisted-two-type-typical-typically-tyre-the-ugly-ultimate-ultimately-umbrella-unable-unacceptable-uncertain-uncle-uncomfortable-unconscious-uncontrolled-under-underground-underneath-understand-understanding-underwater-underwear-undo-unemployed-unemployment-unexpected-unexpectedly-unfair-unfairly-unfortunate-unfortunately-unfriendly-unhappy-uniform-unimportant-union-unique-unit-unite-united-universe-university-unkind-unknown-unless-unlike-unlikely-unload-unlucky-unnecessary-unpleasant-unreasonable-unsteady-unsuccessful-untidy-until-unusual-unusually-unwilling-unwillingly-up-upon-upper-upset-upsetting-upside-upstairs-upward-upwards-urban-urge-urgent-us-use-used-useful-useless-user-use-usual-usually-vacation-valid-valley-valuable-value-van-variation-varied-variety-various-vary-vast-vegetable-vehicle-venture-version-vertical-very-via-victim-victory-video-view-village-violence-violent-violently-virtually-virus-visible-vision-visit-visitor-vital-vocabulary-voice-volume-vote-wage-waist-wait-waiter-wake-walk-walking-walk-wall-wallet-wander-want-war-warm-warmth-warm-warn-warning-wash-washing-wash-waste-watch-water-wave-way-we-weak-weakness-wealth-weapon-wear-weather-web-website-wedding-wednesday-week-weekend-weekly-weigh-weight-welcome-well-west-western-wet-what-whatever-wheel-when-whenever-where-whereas-wherever-whether-which-while-whisper-whistle-white-who-whoever-whole-whom-whose-why-wide-widely-width-wife-wild-wildly-will-willing-willingly-willingness-win-wind-window-wine-wing-winner-winning-winter-wire-wise-wish-with-withdraw-within-without-witness-woman-wonder-wonderful-wood-wooden-wool-word-work-worker-working-work-world-worried-worry-worrying-worse-worship-worst-worth-would-wound-wounded-wrap-wrapping-wrist-write-writer-writing-written-wrong-wrongly-yard-yawn-yeah-year-yellow-yes-yesterday-yet-you-young-your-yours-yourself-youth-zero-zone-'
dic = stng.split('-')
def is_ascii(s):
    return all(ord(c) < 128 for c in s)
#########################<CLASS NODE>##################
class Node(object):
#-----------------------------------------------
    def __init__(self, value):
        self.value = value
        self.children = {}

    def prnt(self, stng):
        if self.value=='$': 
            return
        for node in self.children:
            self.children[node].prnt(stng+node)
        return

    def display(self):
        if self.value =='$': return
        for char in self.children:
            (self.children[char]).display()
#------------------------------------------------
    def insert(self, stng):
        if is_ascii(stng):
            if stng=='':
                p = Node('$')
                self.children[p.value]=p
                return
            if stng[0] in self.children:
                self.children[stng[0]].insert(stng[1:])
                return
            if stng[0] not in self.children:
                p = Node(stng[0])
                self.children[p.value]=p
                p.insert(stng[1:])
                return
        return
    def search(self, stng):
        for child in self.children:
            if child=='$' and stng=='':
                return True
            if len(stng)>0:
                if child==stng[0]:
                    return self.children[child].search(stng[1:])
        return False

    def randomChild(self):
        return choice(list(self.children.keys()))

    def searchForNextLetter(self, stng):
        for child in self.children:
            if stng=='':
                return self.randomChild()
            if len(stng)>0:
                if child==stng[0]:
                    return self.children[child].searchForNextLetter(stng[1:])
        return stng

    def fragmentInDictionary(self, stng):
        if stng=='':
            return True
        for child in self.children:
            if len(stng)>0:
                if child==stng[0]:
                    return self.children[child].fragmentInDictionary(stng[1:])
        return False


def createTrieFromDictionaryFile():
    root = Node('*')
    for word in dic:
        root.insert(word)
    return root
#--------------------------------------------------------------------------------
def countLetterFrequency(dic):
    letterArray = []
    total_char_count=0
    for i in range(128):
        letterArray.append(0) 
    a = 1
    for line in dic:
        if is_ascii(line):
            for char in line:
                letterArray[ord(char)]+=1 
                total_char_count+=1
    return (letterArray, total_char_count)
def createCharacterRatingArray():
	scores = []
	for i in range(128):
		scores.append(0) 
	data = countLetterFrequency(dic)
	frequencies = data[0]
	total_char_count=data[1]
	asciiIndexIterator=0
	for freq in frequencies:
		scores[asciiIndexIterator]= (1-(freq/total_char_count))
		asciiIndexIterator+=1


	return scores
#----------------------------------------------------------------------

def printMatrix(matrix):
	print(' _ _ _ _ _ _ _ _ _ _ ')
	for row in matrix:
		for col in row:
			print ('|' + col, end='')
		print('|')    
	print('| - - - - - - - - - |')


#----------------------------------------------------------------------
def spaceForWords(ch, matrix, tup, root, scores):
	upRightPath = []
	upLeftPath = []
	rightPath = []
	leftPath = []
	downPath = []
	upPath = []
	downLeftPath = []
	downRightPath = []
	if tup[0]<9 and tup[1]<9:
		x=tup[0]+1
		y=tup[1]+1
		downRightPath+=[matrix[x][y]]
		x+=1
		y+=1
		while x<9 and y<9:
			downRightPath+=[matrix[x][y]]
			x+=1
			y+=1
	if tup[0]<9 and tup[1]>0:
		x=tup[0]+1
		y=tup[1]-1
		downLeftPath+=[matrix[x][y]]
		x+=1
		y-=1
		while x<9 and y>0:
			downLeftPath+=[matrix[x][y]]
			x+=1
			y-=1
		
	if tup[0]>0 and tup[1]>0:
		x=tup[0]-1
		y=tup[1]-1
		upLeftPath+=[matrix[x][y]]
		x-=1
		y-=1
		while x>0 and y>0:
			upLeftPath+=[matrix[x][y]]
			x-=1
			y-=1
	if tup[0]>0 and tup[1]<9:
		x=tup[0]-1
		y=tup[1]+1
		upRightPath+=[matrix[x][y]]
		x-=1
		y+=1
		while x>0 and y<9:
			upRightPath+=[matrix[x][y]]
			x-=1
			y+=1
	if tup[1]<9:
		x=tup[0]
		y=tup[1]+1
		rightPath+=[matrix[x][y]]
		y+=1
		while y<9:
			rightPath+=[matrix[x][y]]
			y+=1
	if tup[1]>0:
		x=tup[0]
		y=tup[1]-1
		leftPath+=[matrix[x][y]]
		y-=1
		while y>0:
			leftPath+=[matrix[x][y]]
			y-=1
	if tup[0]<9:
		x=tup[0]+1
		y=tup[1]
		downPath+=[matrix[x][y]]
		x+=1
		while x<9 and matrix[x][y]=='+':
			downPath+=[matrix[x][y]]
			x+=1
	if tup[0]>0:
		x=tup[0]-1
		y=tup[1]
		upPath+=[matrix[x][y]]
		x-=1
		while x>0 and matrix[x][y]=='+':
			upPath+=[matrix[x][y]]
			x-=1

#----------------------------------------------------------------------

def densityOfBoard(matrix):
	density=0
	for row in matrix:
		for col in row:
			if col=='+':
				density+=1
	return density

#----------------------------------------------------------------------
def evaluateMove(ch, matrix, tup, root, scores):
	upRightPath = []
	upLeftPath = []
	rightPath = []
	leftPath = []
	downPath = []
	upPath = []
	downLeftPath = []
	downRightPath = []
	if tup[0]<9 and tup[1]<9 and matrix[tup[0]+1][tup[1]+1]!='+':
		x=tup[0]+1
		y=tup[1]+1
		downRightPath+=[matrix[x][y]]
		x+=1
		y+=1
		while x<9 and y<9 and matrix[x][y]!='+':
			downRightPath+=[matrix[x][y]]
			x+=1
			y+=1
	if tup[0]<9 and tup[1]>0 and matrix[tup[0]+1][tup[1]-1]!='+':
		x=tup[0]+1
		y=tup[1]-1
		downLeftPath+=[matrix[x][y]]
		x+=1
		y-=1
		while x<9 and y>0 and matrix[x][y]!='+':
			downLeftPath+=[matrix[x][y]]
			x+=1
			y-=1
		
	if tup[0]>0 and tup[1]>0 and matrix[tup[0]-1][tup[1]-1]!='+':
		x=tup[0]-1
		y=tup[1]-1
		upLeftPath+=[matrix[x][y]]
		x-=1
		y-=1
		while x>0 and y>0 and matrix[x][y]!='+':
			upLeftPath+=[matrix[x][y]]
			x-=1
			y-=1
	if tup[0]>0 and tup[1]<9 and matrix[tup[0]-1][tup[1]+1]!='+':
		x=tup[0]-1
		y=tup[1]+1
		upRightPath+=[matrix[x][y]]
		x-=1
		y+=1
		while x>0 and y<9 and matrix[x][y]!='+':
			upRightPath+=[matrix[x][y]]
			x-=1
			y+=1
	if tup[1]<9 and matrix[tup[0]][tup[1]+1]!='+':
		x=tup[0]
		y=tup[1]+1
		rightPath+=[matrix[x][y]]
		y+=1
		while y<9 and matrix[x][y]!='+':
			rightPath+=[matrix[x][y]]
			y+=1
	if tup[1]>0 and matrix[tup[0]][tup[1]-1]!='+':
		x=tup[0]
		y=tup[1]-1
		leftPath+=[matrix[x][y]]
		y-=1
		while y>0 and matrix[x][y]!='+':
			leftPath+=[matrix[x][y]]
			y-=1
	if tup[0]<9 and matrix[tup[0]+1][tup[1]]!='+':
		x=tup[0]+1
		y=tup[1]
		downPath+=[matrix[x][y]]
		x+=1
		while x<9 and matrix[x][y]!='+':
			downPath+=[matrix[x][y]]
			x+=1
	if tup[0]>0 and matrix[tup[0]-1][tup[1]]!='+':
		x=tup[0]-1
		y=tup[1]
		upPath+=[matrix[x][y]]
		x-=1
		while x>0 and matrix[x][y]!='+':
			upPath+=[matrix[x][y]]
			x-=1
	# if densityOfBoard(matrix)>75:
	arr1 = downRightPath[::-1]
	arr1.append(ch)
	arr1 = arr1+upLeftPath
	words1 = findWords(arr1, len(downRightPath), root, scores, matrix)

	arr1 = downLeftPath[::-1]
	arr1.append(ch)
	arr1 = arr1+upRightPath
	words1 += findWords(arr1, len(downLeftPath), root, scores, matrix)

	arr1 = downPath[::-1]
	arr1.append(ch)
	arr1 = arr1+upPath
	words1 += findWords(arr1, len(downPath), root, scores, matrix)

	arr1 = rightPath[::-1]
	arr1.append(ch)
	arr1 = arr1+leftPath
	words1 += findWords(arr1, len(rightPath), root, scores,matrix)
	score = 0
	for word in words1:
		score+=int(word)
	# else:
	# 	arr1 = downRightPath[::-1]
	# 	arr1.append(ch)
	# 	arr1 = arr1+upLeftPath
	# 	words1 = lateGame(arr1, len(downRightPath), root, scores)

	# 	arr1 = downLeftPath[::-1]
	# 	arr1.append(ch)
	# 	arr1 = arr1+upRightPath
	# 	words1 += lateGame(arr1, len(downLeftPath), root, scores)

	# 	arr1 = downPath[::-1]
	# 	arr1.append(ch)
	# 	arr1 = arr1+upPath
	# 	words1 += lateGame(arr1, len(downPath), root, scores)

	# 	arr1 = rightPath[::-1]
	# 	arr1.append(ch)
	# 	arr1 = arr1+leftPath
	# 	words1 += lateGame(arr1, len(rightPath), root, scores)
	# 	score = 0
	# 	for word in words1:
	# 		score+=scoreWord(word, scores)
	return score
#---------------------------------------------------------------------

def findWords(arr, ind, node, scores, matrix):
	words = []
	fragFactor = 1+(densityOfBoard(matrix)/100.0)
	wholeFactor = 2.5-(densityOfBoard(matrix)/100.0)
	for i in range(len(arr)):
		start = ind-i
		if start>-1:
			for x in range(i+1):
				if start+x>-1 and ind+x<len(arr):
					if node.search(''.join(arr[start+x:ind+x+1]))==True:
						word = wholeFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if node.search(''.join(arr[start+x:ind+x+1][::-1]))==True:
						word = wholeFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if start+x==0 and node.fragmentInDictionary(''.join(arr[start+x:ind+x+1])):
						word = fragFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if ind+x+1==len(arr) and node.fragmentInDictionary(''.join(arr[start+x:ind+x+1][::-1])):
						word = fragFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
		else:
			for x in range(i+1):
				if ind+x+abs(start)<len(arr):
					#----------------------------------------------------------------------
					if node.search(''.join(arr[x:ind+x+abs(start)+1]))==True:
						word = wholeFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if node.search(''.join(arr[x:ind+x+abs(start)+1][::-1]))==True:
						word = wholeFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if x==0 and node.fragmentInDictionary(''.join(arr[x:ind+x+abs(start)+1])):
						word = fragFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
					if ind+x+abs(start)+1 and node.fragmentInDictionary(''.join(arr[x:ind+x+abs(start)+1][::-1])):
						word = fragFactor*scoreWord(''.join(arr[start+x:ind+x+1]), scores)
						words.append(word)
	return words

#--------------------------------------------------------------------------

def lateGame(arr, ind, node, scores):
	words = []
	for i in range(len(arr)):
		start = ind-i
		if start>-1:
			for x in range(i+1):
				if start+x>-1 and ind+x<len(arr):
					if node.search(''.join(arr[start+x:ind+x+1]))==True:
						words.append(''.join(arr[start+x:ind+x+1]))
					if node.search(''.join(arr[start+x:ind+x+1][::-1]))==True:
						words.append(''.join(arr[start+x:ind+x+1][::-1]))
		else:
			for x in range(i+1):
				if ind+x+abs(start)<len(arr):
					if node.search(''.join(arr[x:ind+x+abs(start)+1]))==True:
						words.append(''.join(arr[x:ind+x+abs(start)+1]))
					if node.search(''.join(arr[x:ind+x+abs(start)+1][::-1]))==True:
						words.append(''.join(arr[x:ind+x+abs(start)+1][::-1]))
	return words

#----------------------------------------------------------------------------
def scoreWord(word, scores):
	score = 0
	for ch in word:
		score+=scores[ord(ch)]
	return score

#####################################################################
ROW = 10
COL = 10
    
def bestMove(matrix, tiles, root, scores):
	movesSquared=[]
	rowIter = 0
	moves = []
	for row in matrix:
		colIter = 0	
		for col in row:
			if col=='+':
				for tile in tiles:
					moves.append((evaluateMove(tile, matrix, (rowIter, colIter), root, scores),rowIter, colIter, tile))
			colIter+=1
		rowIter+=1
	moves.sort()
	return max(moves)
def maxMove(matrix, tiles, root, scores):
	rowIter = 0
	moves = []
	for row in matrix:
		colIter = 0	
		for col in row:
			if col=='+':
				for tile in tiles:
					moves.append((evaluateMove(tile, matrix, (rowIter, colIter), root, scores),rowIter, colIter, tile))
			colIter+=1
		rowIter+=1
	return max(moves)
def getAllInputs():
    playerNumber = 0
    tiles = ""
    matrix = [[0 for c in range(COL)]
                    for r in range(ROW)]
    player1Score = 0
    player2Score = 0
    
    for i in range(0,13):
        if i == 0:
            playerNumber = int(float(input()))
        if i == 1:
            tiles = input().split(' ')
        if (i < 12 and i >= 2):
            rowValues = list(input())
            
            for c in range(COL):
                matrix[i - 2][c] = rowValues[c]
        if i == 12:
            scores = input().split(' ')
            
            player1Score = scores[0]
            player2Score = scores[1]

    return playerNumber, tiles, matrix, player1Score, player2Score
    
    
def findAllWords():
    root = Node('*')
    file1 = open ('Dictionary.txt')
    for word in file1:
        root.insert(word.lower().strip())
    return root
def boardFull(matrix):
	count = 0
	for row in matrix:
		for col in row:
			if col=='+':
				count+=1
	if count==0:
		exit(0)
	return

def bestPiece():
    return
def main():
	root = createTrieFromDictionaryFile()
	root.display()
	total_char_count=0
	countLetterFrequency(dic)
	scores = createCharacterRatingArray()
	playerNumber, tiles, matrix, player1Score, player2Score = getAllInputs()

	move = bestMove(matrix, tiles, root, scores)
	# boardFull(matrix)
	if move[0]==0:
		arr = ['a','e','i','o','u']
		ch = random.choice(arr)
		print(move[1],move[2], ch)
	else:	
		print(move[1], move[2], move[3])
if __name__ == '__main__':
    main()



