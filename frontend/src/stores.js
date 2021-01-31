import {writable} from "svelte/store";

export let tab = writable(0);
export let asn = writable(0);
export let name = writable("");