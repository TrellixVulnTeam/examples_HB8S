SUBDIRS = IPU/custom_ops

.PHONY: all
all:
	@list='$(SUBDIRS)'; for subdir in $$list; do \
		echo "make in $$subdir";\
		$(MAKE) -C $$subdir;\
	done

.PHONY: clean
clean:
	@echo Making clean
	@list='$(SUBDIRS)'; for subdir in $$list; do \
		echo "make in $$subdir";\
		$(MAKE) -C $$subdir clean;\
	done
